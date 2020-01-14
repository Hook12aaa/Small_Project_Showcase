import socket
import time

host = "192.168.1.109"
port = 1567

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
serversocket.bind((host, port)) #Binds to the IP
serversocket.listen(5) #Listens to the port
clientsocket,addr = serversocket.accept()
print("Got a connection {0}".format(addr))

def upload_message(Message):
	clientsocket.send(bytes("Computer", "utf8")+Message)
	time.sleep(0.5)
	clientsocket.close()

while True:
	upload_message("Hello")
	time.sleep(2)
	upload_message("World")