# python3
import socket

ip = "127.0.0.1"

#ip="192.168.41.44"
port = 5050

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))


i=0
while True:
	data, addr = s.recvfrom(2048)
	print ("Received from ",addr)
	#print ("Received  ",str(data))
	p=data.decode()
	#print(p)
	if p:
		x="Acknowledged!"
	s.sendto(x.encode(),addr)
s.close()
