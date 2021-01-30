import socket
import sys
import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Required: Script, IP address, Port number")
    exit()

ip_address = str(sys.argv[1])
port = int(sys.argv[2])
server.bind((ip_address, port)) 

server.listen(4)

clients = []

def clientthread(connection, address):
    
    welcome = "Welcome"
    connection.sendall(welcome.encode('utf-8'))



    while True:
            try:     
                msg = connection.recv(2048)    
                if msg:
                    print(address[0] + ": " + msg)
                    broadcast_msg = address[0] + ": " + message
                    broadcast(broadcast_msg, connection)

                else:
                    remove(connection)
            except:
                continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.sendall(message.encode('utf-8'))
            except:
                client.close()
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

while True:
    connection, address = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    clients.append(connection)
    print(address[0] + " connected")

    _thread.start_new_thread(clientthread, (connection, address))


connection.close()
server.close()