import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 12345))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: 
            break
        from_client += data
	print ("Message from client: ")
        print from_client
        x = raw_input("Enter response: ")
        conn.send(x)
    conn.close()
    print 'client disconnected'
