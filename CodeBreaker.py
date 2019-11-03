import requests,re
from bs4 import BeautifulSoup

class Validator():
	"""Dictionary Validator. Just parse the keyword into the IsINDictionary Methood and it will return true or false.
	**Warning this needs internet connection!**
	 """
	def get_soup_object(url):
		return BeautifulSoup(requests.get(url).text,features="html.parser")

	def IsInDictionary(Cypher_Results):
		"""Dictionary Validator. Just parse the keyword and it will return true or false.
		**Warning this needs internet connection!**
		"""
		if len(Cypher_Results.split()) > 1:
		    print("Error: A Cypher_Results must be only a single word")
		else:
			html =Validator.get_soup_object("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
			    Cypher_Results))
			if str(html.findAll("h3")[0]) == "<h3>Your search did not return any results.</h3>":
				return False
			else:
				return True


class CeaserCypherOnlyChar():
	"""This uses simple ceaser cipher with sticking inside the 
	charracter range. You can brute force and decode text. Allowing you
	to see what is hidden away. This doesn't use any imports"""
	def KnownKey(Cypher,key):
		""" Enter Your Cyphered Text and the key. It will return the dycripted file
		Format  is KnownKey(InsertCypher,InsertKey)"""
		def Shift(letter,key):
			ShiftedLetter = ord(letter) + key
			if ShiftedLetter > 122:
				ShiftedLetter -= 26
			return ShiftedLetter

		def CharOrNot(letter):
			if ord(letter) > 96 and 123 > ord(letter):
				return True
			else:
				return False

		CompletedString = ""
		for letter in Cypher.lower():
			if CharOrNot(letter) is True:
				CompletedString += chr(Shift(letter,key))
			if CharOrNot(letter) is False:
				CompletedString += letter
		return CompletedString

	def BruteForce(Cypher= "InsertText"):
		"""prints an output and number so you can find the key."""
		for i in range(29):
			print("Number:{} Text:{}".format(i,CeaserCypherOnlyChar.KnownKey(Cypher,key = i)))

	def BrueForceWithValidator(Cypher = "InsertText"):
		""" Just Parse in the cyphered text and it will return a key and the orginal text"""
		for i in range(29):
			Output = CeaserCypherOnlyChar.KnownKey(Cypher,key = i)
			if Validator.IsInDictionary(Output) is True:
				return [i,Cypher,Output]


if __name__ == '__main__':
	# Here is an example on how to decode a ceaser ciphered tex
	Results = CeaserCypherOnlyChar.BrueForceWithValidator("QWHUUT")
	print("Key:{}, Cyphered:{}, Output:{}".format(Results[0],Results[1],Results[2]))
