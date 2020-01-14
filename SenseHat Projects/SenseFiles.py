from sense_hat import SenseHat
import socket
import time

sense = SenseHat()

class SenseHatInput():

	def temperature(self):
		Input = str(int(round(sense.get_temperature())))
		return Input

	def humidity(self):
		Input = str(int(round(sense.get_humidity())))
		return Input
	def ip_address(self):
		try:
			IPSOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			IPSOCKET.connect(("8.8.8.8", 80))
			return str(IPSOCKET.getsockname()[0])
			IPSOCKET.close()
		except Exception as error:
			print(error)

class Symbols():
	"""docstring for Symbols"""
	def __init__(self):
		self.B=[0,0,255]
		self.R=[255,0,0]
		self.G=[0,255,0]
		self.W=[255,255,255]
		self.C = [0,0,0]
	def WIFISymbol(self):
		WIFIMenu= [
		self.W, self.W, self.W, self.W, self.W, self.W, self.W, self.W,
		self.W, self.W, self.W, self.W, self.W, self.W, self.W, self.W,
		self.W, self.B, self.B, self.B, self.B, self.B, self.B, self.W,
		self.B, self.W, self.W, self.W, self.W, self.W, self.W, self.B,
		self.W, self.W, self.B, self.B, self.B, self.B, self.W, self.W,
		self.W, self.B, self.W, self.W, self.W, self.W, self.B, self.W,
		self.W, self.W, self.W, self.B, self.B, self.W, self.W, self.W,
		self.W, self.W, self.W, self.B, self.B, self.W, self.W, self.W
		]
		return WIFIMenu

	def TempSymbol(self):
		TempMenu= [
		self.C, self.C, self.C, self.W, self.W, self.C, self.C, self.C,
		self.C, self.C, self.W, self.R, self.R, self.W, self.C, self.C,
		self.C, self.C, self.W, self.R, self.R, self.W, self.C, self.C,
		self.C, self.C, self.W, self.R, self.R, self.W, self.C, self.C,
		self.C, self.C, self.W, self.R, self.R, self.W, self.C, self.C,
		self.C, self.W, self.R, self.B, self.B, self.R, self.W, self.C,
		self.C, self.W, self.R, self.B, self.B, self.R, self.W, self.C,
		self.C, self.C, self.W, self.W, self.W, self.W, self.C, self.C
		]
		return TempMenu

	def HumSymbol(self):
		HumidityMenu= [
		self.C, self.C, self.C, self.C, self.C, self.C, self.C, self.C,
		self.C, self.C, self.C, self.W, self.W, self.C, self.C, self.C,
		self.C, self.C, self.W, self.B, self.B, self.W, self.C, self.C,
		self.C, self.W, self.B, self.B, self.B, self.B, self.W, self.C,
		self.C, self.W, self.B, self.B, self.B, self.B, self.W, self.C,
		self.C, self.W, self.B, self.B, self.B, self.B, self.W, self.C,
		self.C, self.C, self.W, self.B, self.B, self.W, self.C, self.C,
		self.C, self.C, self.C, self.W, self.W, self.C, self.C, self.C
		]
		return HumidityMenu
	def StartSymbol(self):
		Starting= [
		self.C, self.C, self.C, self.C, self.C, self.C, self.C, self.C,
		self.C, self.B, self.B, self.C, self.C, self.B, self.B, self.C,
		self.C, self.B, self.B, self.C, self.C, self.B, self.B, self.C,
		self.C, self.C, self.C, self.C, self.C, self.C, self.C, self.C,
		self.C, self.B, self.C, self.C, self.C, self.C, self.B, self.C,
		self.C, self.B, self.C, self.C, self.C, self.C, self.B, self.C,
		self.C, self.C, self.B, self.B, self.B, self.B, self.C, self.C,
		self.C, self.C, self.C, self.C, self.C, self.C, self.C, self.C
		]
		return Starting