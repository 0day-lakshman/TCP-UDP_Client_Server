import socket

TCP_PORT = 24000
IP_ADDR = '127.0.0.15'
BUF_SIZE = 1024

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
k.connect((IP_ADDR, TCP_PORT))
MSG = "Hello, I am the Client!"
k.send(MSG.encode())
data = k.recv(BUF_SIZE)
print(data.decode())
k.close()