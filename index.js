PORT = 40000;
HOST = '192.168.0.1';

// var UdpControl = require('./control');

// var cont = new UdpControl({});
var dgram = require('dgram');
var debug = require('simple-debug')('udpcontrol');
var Events = require('events');

events = new Events();
client = dgram.createSocket('udp4');
client.bind(6000);
NOTCONNECTED = 4;

function send(serialized){
    serialized = serialized.split(':').join('');
    debug(serialized.replace('\r', '|'));
    var buffer = new Buffer(serialized,'hex');
    client.send(buffer, 0, buffer.length, PORT, HOST);
}

function connect(){
  if(NOTCONNECTED){
    var serialized = '63:63:01:00:00:00:00'
    send(serialized);
    NOTCONNECTED--;
    setTimeout(connect,1000);
    if(!NOTCONNECTED){events.emit('connected');}
  } else {
    var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
    send(serialized)
    setTimeout(connect,40);
  }
}


events.on('takeoff', () => {
  var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:3c:bc:99';
  send(serialized);
});

events.on('land', () => {
  var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:1c:9c:99'
  send(serialized);
});

events.on('kill', () => {
  var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:2c:ac:99';
  send(serialized);
});

events.on('connected', () => {
  events.emit('takeoff');
  setTimeout(function(){events.emit('land');},10);
});

connect()


if(!NOTCONNECTED){
  console.log('connected')
}
// cont.connect();

// while(cont.notconnected){
//   // do nothing
// }

// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:2c:ac:99'
// cont.send(serialized)
//
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:3c:bc:99'
// cont.send(serialized)
//

// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
// send(client,serialized)
//
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
// send(client,serialized)
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
// send(client,serialized)
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
// send(client,serialized)
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
// send(client,serialized)
//
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:3c:bc:99'
// send(client,serialized)
//
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:2c:ac:99'
// send(client,serialized)

// , function(err, bytes) {
//     if (err) throw err;
//     console.log('UDP message sent to ' + HOST +':'+ PORT);
//     client.close();
// }
