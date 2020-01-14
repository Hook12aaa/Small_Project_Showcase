
#-=(    Import section    )=-#
from LogMaker import Logmaker
from Progress_Bar_File import Progress_Bar 
import EmailServer
import socket
import time

#-=(   Hostname and Port   -=)#
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = "10.101.2.34"
port = 13
#-----------------------------#

def RunBlue():
	enter_log("Lesson Cancelled","MailLog")
	Upload_message("Blue")

def RunRed():
	enter_log("New Homework has been assighned to student Anton Chepaldin","MailLog")
	Upload_message("Red")

def RunGreen():
	enter_log("Results has been published to Anton Chepaldin","MailLog")
	Upload_message("Green")

def Upload_message(Message):
	enter_log("Uploading Message {}\n Over IP {}\n and Port {}".format(Message,host,port),"MailLog")
	serversocket.bind((host, port)) #Binds to the IP
	serversocket.listen(5) #Listens to the port
	while True:
		clientsocket,addr = serversocket.accept()
		print("Got a connection {0}".format(addr))
		clientsocket.send(Message.encode('ascii'))
	clientsocket.close()
	
def intervial_check():
	Mail = EmailServer.Email("displayemailpi@gmail.com","Raspb3rry","imap.gmail.com","Inbox")
	KeyWords = [["loa","Blue"],["homework","Red"],["results","Green"]]
	NewMail = Mail.ReturnsEmail()
	print(NewMail)
	for i,mail in  enumerate(NewMail):
		if mail.lower() == KeyWords[i][0]:
			exec("Run{0}()".format(KeyWords[i][1]))

while True:

	for i in range(100):
		Progress_Bar.update_progress_bar(i/100.0,Messsage = "Current Wait Time")
		time.sleep(0.5)
	try:
		intervial_check()
	except Exception as e:
		enter_log("There is an error {0}".format(e),"MailLog")
		input("There is an error {0}".format(e))