import socket
IP = ''
PORT = 6000
BUFFER_SIZE = 2056

f = open('stream.h264', 'wb')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((IP,PORT))

while True:
    data = sock.recv(BUFFER_SIZE)
    print(data)
    f.write(data)
    # print("Writing")
sock.close()
f.close()
