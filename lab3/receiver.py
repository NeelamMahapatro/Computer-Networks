import socket
import time
import sys

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 6789))
serv.listen(1)
flag = True
start = time.time()
packet_size = 0
while True:
    conn, addr = serv.accept()
    from_sender = ''
    while True:
        data = conn.recv(4096)
	packet_size+=sys.getsizeof(data)
        if not data: 
            break
        from_sender = data
	print ("Message from Sender: ")
        print from_sender
	end = time.time()
        #time.sleep(2)
        x = "ACK"
        if(flag):
	    time.sleep(1)
            conn.send(x)
            flag = False
        else:
	    flag = True
        throughput = (packet_size*8/((end-start)*1000))
	print(throughput)
    conn.close()
    #print 'client disconnected'
