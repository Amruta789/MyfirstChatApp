import socket
from socket import socket

host = "10.0.0.16"
port = 5000

server_socket = socket()
server_socket.bind((host,port))
server_socket.listen()
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:
    data=conn.recv(1024).decode()
    print("From connected user: " + str(data))
    data = input(" -> ")
    conn.send(data.encode())
    
conn.close()
