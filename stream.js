
var dgram = require('dgram');
client = dgram.createSocket('udp4');
client.bind(6000);
client.on('message', (msg, rinfo) => {
  var hexmsg = Buffer.from(msg,'utf8').toString('hex')
  if(hexmsg.indexOf('63:63:03:00:00'.split(':').join('')) > -1){
    console.log(`server got: ${hexmsg} from ${rinfo.address}:${rinfo.port}`);
  }
});
