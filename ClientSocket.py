import socket

client = socket.socket()
client.connect(('localhost', 65205))       #ip of the system in which server program is running

while True:
    msg = input("sister: ")
    client.send(bytes(msg, 'utf-8'))
    print(client.recv(1024).decode())