import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))
from_server=""
while True:
    x = raw_input("Enter message: ")
    client.send(x)
    from_server = client.recv(4096)
    print ("Message from server: ")
    print from_server
    if(from_server == "exit"):
        break
client.close()
print from_server
