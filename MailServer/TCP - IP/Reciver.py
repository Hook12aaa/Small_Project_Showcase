import socket
import time
host = "192.168.1.109"
port = 1567
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



s.connect((host,port))
data = ""
while True:
	data = s.recv(1024)
	if data != None:
		print("Received: {}".format(data))
	time.sleep(5)

s.close()