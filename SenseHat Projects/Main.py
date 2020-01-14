from sense_hat import SenseHat
from SenseFiles import *
import time
sense = SenseHat()
Symbols = Symbols()
SenseHatInput = SenseHatInput()

SymbolList = [Symbols.TempSymbol(),Symbols.HumSymbol(),Symbols.WIFISymbol()]
Options = ["WIFI()","Temp()","Hum()"]
PrintedSymbol = 0
Input = None

def WIFI():
	sense.show_message(SenseHatInput.temperature())

def Temp():
	sense.show_message(SenseHatInput.humidity())

def Hum():
	IP = list(SenseHatInput.ip_address())
	for num,SelectedNumber in enumerate(IP):
		printedIP = IP[num]
		sense.show_letter(printedIP,(0,0,255),(255,255,255))
		time.sleep(1)

sense.show_message("Good Day Anton!")
sense.set_pixels(Symbols.StartSymbol())
time.sleep(5)

while True:
	for event in sense.stick.get_events():
		if event.action =="pressed":
			if event.direction == "up":
				if PrintedSymbol == len(SymbolList):
					PrintedSymbol = 0
				else:
					PrintedSymbol += 1
			if event.direction == "down":
				if PrintedSymbol == -3:
					PrintedSymbol = 2
				else:
					PrintedSymbol += -1
			if event.direction == "middle":
				exec("{0}".format(Options[PrintedSymbol]))
			if PrintedSymbol == len(SymbolList):
				PrintedSymbol = 0
		print("Direction: {0} Action: {1} Input: {2} PrintedSymbol: {3}".format(event.direction, event.action,Input,PrintedSymbol))

	exec("sense.set_pixels({0})".format(SymbolList[PrintedSymbol]))