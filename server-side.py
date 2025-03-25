import socket
import threading
import sys

# get address and port as input
ip_address = sys.argv[1] 
port = int(sys.argv[2]) 

# set up server using socket and start listening
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, port))
server.listen()

# create list for clients
list_of_clients = []

# function to get message and send to other clients
def threadClients (client):
    while True:
        message = client.recv(1024).decode()  
        for client_in_list in list_of_clients:
            if client_in_list != client:  
                client_in_list.send(message.encode())

    list_of_clients.remove(client)
    client.close()

print(f"Chat Room Now Running on {ip_address}:{port}")
while True:
    client, _ = server.accept()  
    list_of_clients.append(client)
    threading.Thread(target=threadClients, args=(client,)).start() 
