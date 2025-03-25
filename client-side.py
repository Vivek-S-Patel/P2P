import socket
import threading
import sys

# take address and port as input
ip_address = sys.argv[1]  
port = int(sys.argv[2])   

# set up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip_address, port))  # Connect to the server

# function to get messages and print
def getMessage():
    while True:
        message = server.recv(1024).decode()  
        print("\n" + message)  

# get and start threading
getThread = threading.Thread(target = getMessage, daemon = True)
getThread.start()

while True:
    message = input()  
    server.send(message.encode())  
