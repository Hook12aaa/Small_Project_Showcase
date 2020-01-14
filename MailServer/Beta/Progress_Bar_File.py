import sys
import time

class Progress_Bar():
	"""-={Progress Bar}=-
	What this does it will rewrite a progress screen every inteveral where it is called.
	This is so after a completed action you can have the program auto update with even a differenct message.
	I built this to give a better print out as it makes everyones life easier.

	To Run:

	Call update_progress_bar(progress,Message,info). Replace Progress and Message
	to what you want and you can even dislay info to the user on the current process it's du
	to help when it comes to bug testing or just plain making life easier.

	If you want colour do the same thing but use update_colour_progress_bar()."""
	def __init__():
		pass
	def update_progress_bar(progress,barLength = 10, Messsage = "Current Progress"):
		"""	Call update_progress_bar(progress,Message,info). Replace Progress and Message
		to what you want and you can even dislay info to the user on the current process it's du
		to help when it comes to bug testing or just plain making life easier.
		"""
		block = int(round(barLength*float(round(progress,0))))
		sys.stdout.write("\r {2}: -=[{0}]=- ({1}%)".format( "#"*block + "-"*(barLength-block), round(progress*100,0),Messsage))
		sys.stdout.flush()

	def update_colour_progress_bar(progress,barLength = 10, Messsage = "Current Progress"):
		"""	Call update_colour_progress_bar(progress,Message,info). Replace Progress and Message
		to what you want and you can even dislay info to the user on the current process it's du
		to help when it comes to bug testing or just plain making life easier.
		"""
		block = int(round(barLength*float(progress)))
		sys.stdout.write("\rProgress: \033[1;31;40m-=[\033[1;33;40m{0}\033[1;31;40m]=-\033[1;34;40m ({1}%)\033[1;30;40m".format( "#"*block + "-"*(barLength-block), round(progress*100,0)))
		sys.stdout.flush()

	
	
	def Example():
		for i in range(100):
			time.sleep(1)
			Progress_Bar.update_progress_bar(i/100.0)

Progress_Bar.Example()