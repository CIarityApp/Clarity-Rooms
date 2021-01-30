import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Required: Script, IP address, Port number")
    exit()


ip_address = str(sys.argv[1])
port = int(sys.argv[2])
server.connect((ip_address, port))

while True:
    sockets_list = [server]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets + [sys.stdin]:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.sendall(message.encode('utf-8'))
            sys.stdout.write("You: ")
            sys.stdout.write(message)
            sys.stdout.flush()


server.close()












