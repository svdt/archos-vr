
const dgram = require('dgram');
const debug = require('simple-debug')('udpcontrol');
const Events = require('events');
const Window = require('window');
events = new Events();


const calculateXORChecksum = hex =>
  hex.split(':').reduce((checksum, item) =>
    checksum ^ parseInt(item, 16)
  , 0).toString(16)

module.exports = UdpControl;
function UdpControl(options) {
  this.client = dgram.createSocket('udp4');
  this.client.bind(6000);
  this.notconnected = 4;
  this.port = 40000;
  this.host = '192.168.0.1';
  this.defaultTimeout = 500;
  this.pre = '63:63:0a:00:00:0b:00:66:';
  this.past = ':99';
  this.connreq = '63:63:01:00:00:00:00';
  this.statebk = '80:80:80:80:80:80:80:0c';
  this.state = '80:80:80:80:80:80:80:0c';
  this.frame = '';
  this.window = new Window();
  this.div = this.window.document.createElement('div');
  // setInterval(this.connect, 100);
  var t = this;
  this.connection = setInterval(function(){t.connect();}, 40);
  this.client.on('message', (msg, rinfo) => {
    this.frame += msg;
    var a = this.frame.lastIndexOf("ffd8");
    var b = this.frame.lastIndexOf("ffd9");
    if(a!=-1 && b!=-1){
      var jpg = this.frame.substring(a,b+2);
      this.frame = this.frame.substring(b+2,-1);
      console.log(jpg);
      this.div.innerHTML = '<img src="data:image/jpeg;base64,'+Buffer.from(jpg).toString('base64')+'"/>';
    }
    // res.write('<html><body>')
    // res.write(Buffer.from(data).toString('base64'));
    // res.end('"/></body></html>');
    // var hexmsg = Buffer.from(msg,'utf8').toString('hex')
    // var buffer = new Buffer(hexmsg,'hex');
    // if(hexmsg.indexOf('63:63:03:00:00'.split(':').join('')) > -1){
    //
    //   // console.log(`server got: ${this.client.getRecvBufferSize()} from ${rinfo.address}:${rinfo.port}`);
    // }
  });
}


UdpControl.prototype.send = function(serialized){
  if(serialized.length>20){
    serialized = this.pre+serialized+':'+calculateXORChecksum(serialized)+this.past;
  }
  serialized = serialized.split(':').join('');
  // console.log(serialized);
  // debug(serialized.replace('\r', '|'));
  var buffer = new Buffer(serialized,'hex');
  this.client.send(buffer, 0, buffer.length, this.port, this.host);
}

UdpControl.prototype.connect = function(){
  if(this.notconnected){
    this.send(this.connreq);
    this.notconnected--;
    // if (!this.notconnected){
    //   events.emit('connected');
    // }
    // var t = this;
    // setTimeout(function(){t.connect();},this.defaultTimeout);
  } else {
    // self.keepalive();
    this.send(this.state);
    // var t = this;
    // setTimeout(function(){t.connect();},this.defaultTimeout);
  }
}
