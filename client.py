import socket
from socket import socket

host = "10.0.0.16"
port = 5000

client_socket = socket()
client_socket.connect((host,port))

message = input(" -> ")

while message.lower().strip() != 'bye':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("Received from server: " + data)
    message = input(" -> ")
    
client_socket.close()
