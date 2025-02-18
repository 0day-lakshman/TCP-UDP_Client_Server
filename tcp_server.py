import socket

TCP_PORT = 24000
IP_ADDR = '127.0.0.15'
BUF_SIZE = 30

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
k.bind((IP_ADDR, TCP_PORT))
k.listen(1)
con, addr = k.accept()
print ("Connection Address is : " , addr)
data = con.recv(BUF_SIZE)
print ("Received data : ", data.decode())
msg = "Hi, I am the Server!".encode()
con.send(msg)
con.close()