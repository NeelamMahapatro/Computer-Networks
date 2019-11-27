# python3
import socket
import time

#ip = "192.168.43.56"
ip="127.0.0.1"
port = 5050
i=0
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.sendto(b'116CS0176: Hello',(ip,port))
for i in range(100):
    #x=input()
    x=str(i)
    t0=time.time()
    s.sendto(x.encode(),(ip,port))
    #print("Sending data")
    tt=time.time()-t0
    ack,addr=s.recvfrom(2048)
    #print("Received")
    pd=time.time()-t0-tt
    eta=tt/(tt+2*pd)
    if i==0:
	eff=eta
    elif eff<eta:
	eff=eta
    
print("Throughput efficiency= ",eff)
s.close()
