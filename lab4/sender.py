# python3
import socket


def chunkstring(string, length):
	return (string[0+i:length+i] for i in range(0, len(string), length))

ip='127.0.0.1'
port = 5001

print('Enter data')
inputString=input()

windowSize=4

stringList=list(chunkstring(inputString,windowSize-1))
l=len(stringList)
pos=0

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(0,l):
    pos = pos+1
    x=str(pos)+stringList[i]
    s.sendto(x.encode(),(ip,port))

s.close()
