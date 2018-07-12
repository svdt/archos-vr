"use strict";

const net = require('net')
const dgram = require('dgram')
const WSServer = require('uws').Server
const Split = require('stream-split')
const NALSeparator = new Buffer([0, 0, 0, 1])
const express = require('express')
const systemd = require('systemd')
const app = express()

var wsServer, conf = require('nconf'),
  headers = []
conf.argv().defaults({
  tcpport: 8000,
  udpport: 8000,
  wsport: 8081,
  queryport: false,
  limit: 150
})

if (conf.get('queryport')) {
  app.get('/', (req, res) => {
    var count = 0
    wsServer.clients.forEach((ws) => {
      if (ws.readyState == 1) {
        count++
      }
    })
    res.set('Content-type', 'text/plain')
    res.send(count.toString())
  })
  app.listen(conf.get('queryport'))
}

function broadcast(data) {
  wsServer.clients.forEach((ws) => {
    if (ws.readyState === 1) {
      ws.send(data, { binary: true })
    }
  })
}

if (conf.get('tcpport')) {
  const tcpServer = net.createServer((socket) => {
    console.log('streamer connected')
    socket.on('end', () => {
      console.log('streamer disconnected')
    })
    headers = []
    const NALSplitter = new Split(NALSeparator)
    NALSplitter.on('data', (data) => {
      if (wsServer && wsServer.clients.length > 0) {
        if (headers.length < 3) headers.push(data)
        broadcast(data)
      }
    }).on('error', (e) => {
      console.log('splitter error ' + e)
      process.exit(0)
    })
    socket.pipe(NALSplitter)
  })
  tcpServer.listen(conf.get('tcpport'))
  if (conf.get('tcpport') == 'systemd') {
    console.log('TCP server listening on systemd socket')
  } else {
    var address = tcpServer.address()
    if (address) console.log(
      `TCP server listening on ${address.address}:${address.port}`)
  }
}

const calculateXORChecksum = hex =>
  hex.split(':').reduce((checksum, item) =>
    checksum ^ parseInt(item, 16)
  , 0).toString(16)

var notconnected = 4;
var defaultTimeout = 500;

function send(udpServer,serialized){
  var pre = '63:63:0a:00:00:0b:00:66:';
  var past = ':99';
  if(serialized.length>20){
    serialized = pre+serialized+':'+calculateXORChecksum(serialized)+past;
  }
  serialized = serialized.split(':').join('');
  var buffer = new Buffer(serialized,'hex');
  udpServer.send(buffer, 0, buffer.length, 40000, '192.168.0.1');
}

if (conf.get('udpport')) {
  const udpServer = dgram.createSocket('udp4')

  udpServer.on('listening', () => {
    var address = udpServer.address()
    console.log(
      `UDP server listening on ${address.address}:${address.port}`)
  })
  const NALSplitter = new Split(NALSeparator)
  NALSplitter.on('data', (data) => {
    if (wsServer && wsServer.clients.length > 0) {
      broadcast(data)
    }
  }).on('error', (e) => {
    console.log('splitter error ' + e)
    process.exit(0)
  })
  udpServer.on('message', (msg, rinfo) => {
    NALSplitter.write(msg)
  })
  udpServer.bind(conf.get('udpport'))
  send(udpServer,'63:63:01:00:00:00:00');
  setInterval(function(){
    if(notconnected){
      send(udpServer,'63:63:01:00:00:00:00');
      notconnected--;
    } else {
      send(udpServer,'80:80:80:80:80:80:80:0c');
    }
  }, 40);
}

if (conf.get('wsport')) {
  wsServer = new WSServer({ port: conf.get('wsport') })
  console.log(
    `WS server listening on`, conf.get('wsport')
  )
  wsServer.on('connection', (ws) => {
    if (wsServer.clients.length >= conf.get('limit')) {
      console.log('client rejected, limit reached')
      ws.close()
      return
    }
    console.log('client connected, watching ' + wsServer.clients.length)
    for (let i in headers) {
      ws.send(headers[i])
    }
    ws.on('close', (ws, id) => {
      console.log('client disconnected, watching ' + wsServer.clients.length)
    })
  })
}
