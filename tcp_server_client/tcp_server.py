from socket import socket
from time import ctime 
# create server socket (with socket_family, socket type, protocol=0)
# bind socket to address 
# listen for connections 
# server infinite loop 
    # accept client connection 
    # communication loop 
        # dialog (receive/send) 
    # close client socket
# close server socket gracefully 


HOST = 'localhost'
PORT = 25890
BUFSIZE = 1024 
ADDR = (HOST, PORT)

# socket.bind()
# socket.listen()
# socket.accept()
# socket.recv()

# socket.close()

# create server socket 
tcpServerSocket = socket(AddressFamily = socket.AF_LOCAL)
tcpServerSocket.bind(address = ADDR)
tcpServerSocket.listen()
try: 
    while True:
        print("... waiting for connection...")
        tcpclientSocket, _RetAddress = tcpServerSocket.accept()
        if not data: 
            break
        
        data = tcpclientSocket.recv(bufsize = BUFSIZE)
        tcpclientSocket.sendto(
            data = ('[%s] %s', ctime(), data), 
            address = _RetAddress)
        tcpclientSocket.close()
except: 
    print(Exception)
