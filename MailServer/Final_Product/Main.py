import socket
from communcation_files import *


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = "192.168.1.109"
port = 1457



def RunGreen():
	TCPCommuncator.Upload_Message("Green")

def RunRed():
	TCPCommuncator.Upload_Message("Blue")

def ImportMail():
	SplitMail = ""
	ImportedMail = ["COMPUTING | Summer work 2019 - Year 2","Summer Work","Period 4 Media Lesson 7th Feb - Jack Avery"]
	for i,Imported in enumerate(ImportedMail):
		SplitMail += " "+ Imported
	return SplitMail.split()

Keywords = ["Red","homework"],["Green","LOA"],["Green","Lesson"],["Red","work"]

for Subject in  ImportMail():
	for i,mail in enumerate(Keywords):
		if Subject.lower() == Keywords[i][1].lower():
			exec("Run{}()".format(Keywords[i][0]))