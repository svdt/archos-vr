PORT = 40000;
HOST = '192.168.0.1';

var UdpControl = require('./control');


const calculateXORChecksum = hex =>
  hex.split(':').reduce((checksum, item) =>
    checksum ^ parseInt(item, 16)
  , 0).toString(16)

const pre = '63:63:0a:00:00:0b:00:66:';
const past = ':99';
var cont = new UdpControl({});
var dgram = require('dgram');
var debug = require('simple-debug')('udpcontrol');
var Events = require('events');
var keypress = require('keypress');

events = new Events();
// client = dgram.createSocket('udp4');
// client.bind(6000);
// NOTCONNECTED = 4;
//
// function send(serialized){
//     if(serialized.length>20){
//       serialized = pre+serialized+':'+calculateXORChecksum(serialized)+past;
//     }
//     serialized = serialized.split(':').join('');
//     debug(serialized.replace('\r', '|'));
//     console.log(serialized);
//     var buffer = new Buffer(serialized,'hex');
//     client.send(buffer, 0, buffer.length, PORT, HOST);
// }
//
// function connect(){
//   if(NOTCONNECTED){
//     var serialized = '63:63:01:00:00:00:00'
//     send(serialized);
//     NOTCONNECTED--;
//     setTimeout(connect,1000);
//     if(!NOTCONNECTED){events.emit('connected');}
//   } else {
//     var serialized = '80:80:80:80:80:80:80:0c'
//     send(serialized)
//     setTimeout(connect,40);
//   }
// }


events.on('takeoff', () => {
  cont.state = '80:80:80:80:80:80:80:3c';
  setTimeout(function(){events.emit('standby');},cont.defaultTimeout);
});

events.on('land', () => {
  cont.state = '80:80:80:80:80:80:80:1c'
  setTimeout(function(){events.emit('standby');},cont.defaultTimeout);
});

events.on('kill', () => {
  cont.state = '80:80:80:80:80:80:80:2c';
  setTimeout(function(){events.emit('standby');},cont.defaultTimeout);
});
events.on('standby', () => {
  cont.state = cont.statebk;
});

events.on('connected', () => {
  console.log('connected :)');
  // setTimeout(function(){events.emit('takeoff');},1000);
  // setTimeout(function(){events.emit('land');},5000);
});

cont.connect();

if(!this.notconnected){
  events.emit('connected');
}

// keypress(process.stdin);
// // listen for the "keypress" event
// process.stdin.on('keypress', function (ch, key) {
//   console.log('got "keypress"', key);
//   if (key && key.name == 'up') {
//
//   } else if (key && key.name == 'down') {
//
//   } else if (key && key.name == 'right') {
//
//   } else if (key && key.name == 'left') {
//
//   } else if (key && key.name == 'up') {
//
//   } else if (key && key.ctrl && key.name == 'c') {
//     process.stdin.pause();
//   }
// });
//
// process.stdin.setRawMode(true);
// process.stdin.resume();


// if(!NOTCONNECTED){
//   console.log('connected')
// }
// cont.connect();
//
// while(cont.notconnected){
//   // do nothing
// }
//
// var pre = '63:63:0a:00:00:0b:00:66:';
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:2c:ac:99'
// cont.send(serialized)
//
// var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:3c:bc:99'
// cont.send(serialized)
//
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
//
// , function(err, bytes) {
//     if (err) throw err;
//     console.log('UDP message sent to ' + HOST +':'+ PORT);
//     client.close();
// }
