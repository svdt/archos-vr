#!/usr/bin/env python2.7
import socket,time,sys,cv2,binascii
import numpy as np
from threading import Thread

IP = ''
DST = '192.168.0.1'
DSTP = 40000
PORT = 6000
BUFFER_SIZE = 2048
login = ''.join('63630100000000'.split(':')).decode('hex')
ka = ''.join('63:63:0a:00:00:0b:00:66:80:80:80:80:80:80:80:0c:8c:99'.split(':')).decode('hex')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)

# sock.connect((DST,DSTP))
sock.bind((IP,PORT))
def keepalive():
    sock.sendto(ka,(DST,DSTP))
    time.sleep(0.1)

for i in range(20):
    sock.sendto(login,(DST,DSTP))
    # sock.send(login)
    time.sleep(0.04)

t = Thread(target=keepalive)
t.start()

data = ''
# f = open('stream.h264', 'wb')
while True:
    print('')
    time.sleep(0.1)
#     # sock.sendto(ka,(DST,DSTP))
#     # sock.send(ka)
#     newd = sock.recv(BUFFER_SIZE)
#     if len(newd) != 15 and len(newd) != 106:
#         if len(newd) == 1454:
#             data += newd[54:]
#         elif newd.find('\xff\xd9') != -1:
#             data += newd[52:]
#             a = data.find('\xff\xd8')
#             b = data.find('\xff\xd9')
#             if a == 0 and b == len(data)-2:
#                 jpg = binascii.a2b_hex(data.encode('hex'))
#                 # print(jpg.encode('hex'))
#                 with open('image.jpg', 'wb') as image_file:
#                     image_file.write(jpg)
#                 # i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),1)
#                 # cv2.imshow('i',i)
#             data = ''
#         # a = data.find('\xff\xd8')
#         # b = data.find('\xff\xd9')
#         # if a == 0 and b == len(data)-2:
#         #     jpg = binascii.a2b_hex(data.encode('hex'))
#         #     # print(jpg.encode('hex'))
#         #     i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),1)
#         #     cv2.imshow('i',i)
#         #     data = ''
#     # time.sleep(0.04)
#     # sys.stdout.write(data)
#     # f.write(data)
#     # print(data)
sock.close()
