from datetime import datetime


class Logmaker():
	"""-=  Log Maker  =-

	What is this you may ask? Well it's in the name.
	This program creats a developer log that would 
	print out the message and the timecode. This is
	to help when bug testing programs as it will store
	 the long in a .txt file that people can acesses
	whenever you want.

	-=( enter_log )=-

	To enter a log please call the function in the line of code you want
	and add  in the callables your message like enter_log(instert_message,instert_file_name)
	
	"""
	def LongMakersUpload(file_name,Upload = "Entery"):
		with open(file_name +".txt","a+") as File:
			for line in Upload:
				File.write("Time: {0} Comment: {1}\n".format(datetime.today().strftime("%Y-%m-%d %H,%M,%S"),line))


	def ShortMaker(file_name,Upload = "No Entery"):
		File = open(file_name+".txt","a+")
		File.write("Time: {0} Comment: {1}\n".format(datetime.today().strftime("%Y-%m-%d %H,%M,%S"),Upload))

	def enter_log(Upload,file_name):
		"""
		-=( enter_log )=-
		To enter a log please call the function in the line of code you want
		and add  in the callables your message like enter_log(instert_message,instert_file_name)
		"""
		for l in  list(Upload):
			if l == "\n":
				Logmaker.LongMaker(file_name,Upload)
				break
			else:
				Logmaker.ShortMaker(file_name,Upload)
				break

