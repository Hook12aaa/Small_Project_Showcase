from Mail import Email
from SourceGather import ITDgree
from datetime import datetime
import time

class ARUEMAILS():



	def MyMainProgram():
		def Gather():
			CleanText = ""
			for i in ITDgree.CleanPrintOut():
				CleanText+= "\n{}".format(i)
			CleanText+="\n This is an automated email please do not attempt to reply to it. Provieded by Anton Chepaldin"
			return CleanText

		EmailList =["anton.100chepaldin@gmail.com","spdrake57@gmail.com"]
		SendOut = Email("displayemailpi@gmail.com","Raspb3rry","imap.gmail.com","Inbox")
		for i in EmailList:
			SendOut.SendEmail(Gather(),"Anglia Ruskin University Check at " + datetime.today().strftime("%Y-%m-%d %H,%M,%S"),i,"displayemailpi@gmail.com")
			print("Send Email to {} at {}.".format(i,datetime.today().strftime("%Y-%m-%d %H,%M,%S")))



if __name__ == '__main__':
	while True:
		print("Waiting 10 hours")
		time.sleep(28.800)
		print("Starting Program")
		ARUEMAILS.MyMainProgram()
 