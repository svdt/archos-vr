
var dgram = require('dgram');
var debug = require('simple-debug')('udpcontrol');

module.exports = UdpControl;
function UdpControl(options) {
  this.client = dgram.createSocket('udp4');
  this.client.bind(6000);
  this.notconnected = 4;
  this.port = 40000;
  this.host = '192.168.0.1';
  this.defaultTimeout = 500;
  // client.on('message', (msg, rinfo) => {
  //   var hexmsg = Buffer.from(msg,'utf8').toString('hex')
  //   if(hexmsg.indexOf('63:63:0b:00:00:0f:00:66:64:00'.split(':').join('')) > -1){
  //     console.log(`server got: ${hexmsg} from ${rinfo.address}:${rinfo.port}`);
  //   }
  // });
  //
  // client.on('listening', () => {
  //   const address = client.address();
  //   console.log(`server listening ${address.address}:${address.port}`);
  // });
}


UdpControl.prototype.send = function(serialized){
  serialized = serialized.split(':').join('');
  debug(serialized.replace('\r', '|'));
  var buffer = new Buffer(serialized,'hex');
  this.client.send(buffer, 0, buffer.length, this.port, this.host);
}

// UdpControl.prototype.keepalive = function(){
//   var self = this;
//   var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
//   this.send(serialized)
//   setTimeout(self.keepalive,40)
// }
//
// UdpControl.prototype.connect = function(){
//   var self = this;
//   if(this.notconnected){
//     var serialized = '63:63:01:00:00:00:00'
//     self.send(serialized)
//     this.notconnected--;
//     setTimeout(self.connect,this.defaultTimeout);
//   } else {
//     // self.keepalive();
//     var serialized = '63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'
//     self.send(serialized)
//     setTimeout(self.connect,40);
//   }
// }
