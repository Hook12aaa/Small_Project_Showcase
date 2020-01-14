class cypher_program():
	"""Welecome to the cpyher program built using the fimple ascii encryption.
	To use this you can simple import and bind your module to a varible
	Here are the different modes you have access to
		*"encrpyt(input)" would encrypt anything inside the input variable and reutrn it into a varible
		*"decrpyt(input)" would decrpyt the given input and reutrn it into a varible"	
	Example:
		cypher=cypher_program(199) # Makes the object
		encyrpitword = cypher.encyrpit("Hello World") # Encrpyts the word hello world
		print(encyrpitword) #prints the new encripytion
		decrpyedword= cypher.decrpyt(encyrpitword) # decrpht the chousen word
		print(decrpyedword) # prints orginal veriable
	"""

	def encyrpit(key,Input):
		FinalProduct = ""
		for char in Input:
			FinalProduct +=chr(ord(char)+ key)
		return FinalProduct

	def decrpyt(key,Input):
		FinalProduct = ""
		for char in Input:
			FinalProduct +=chr(ord(char) - key)
		return FinalProduct