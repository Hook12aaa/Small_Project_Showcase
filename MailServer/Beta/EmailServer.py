
import imaplib
import email
class Email():
	"""docstring for Email"""
	def __init__(self,Login,Password,Mail_Server,Inbox,):
		self.Mail = imaplib.IMAP4_SSL(Mail_Server, 993)
		self.Mail.login(Login,Password)
		self.Mail.select(Inbox)
		self.result,self.data = self.Mail.uid("search", None, "ALL") 


	def ReturnsEmail(self):
		self.TotalEmail= []
		for Subject in self.data[0].split():
			self.result, self.data = self.Mail.uid('fetch',Subject, '(RFC822)')
			email_message = email.message_from_bytes(self.data[0][1])
			self.TotalEmail.append(email_message["Subject"])
			self.deleteEmailIMAP(Subject)
		return self.TotalEmail

	def deleteEmailIMAP(self,delate):
		DeleatedEmail = self.Mail.uid('STORE', delate, '+X-GM-LABELS', '\\Trash')
		if DeleatedEmail[0] == "OK":
			self.Mail.expunge()
		else:
			print("Could not expunge as it was not okay.")

Email("displayemailpi@gmail.com","Raspb3rry","imap.gmail.com","Inbox")
    