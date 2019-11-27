import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6789))
from_rcvr=""
flag = True
got = True
x = raw_input("Enter message: ")
while True:
    client.send(x)
    from_rcvr = 0
    t_end = time.time() 
    #while time.time() < t_end:
    if(flag == True):
        from_rcvr = client.recv(4096)
	got = True
        flag = False
    else:
	got = False
	flag = True
        #print("Inside")
        '''if(from_rcvr == "ACK"):
            break
	else:
	    from_rcvr = 0'''
    if(got==False):
        print("Acknowlegement not recieved... Resending message: ")
	print(x)
    else:
        print("ACK Recieved")
        x = raw_input("Enter the next  message: ")
    #if(from_rcvr == "exit"):
        #break
client.close()
print from_rcvr
