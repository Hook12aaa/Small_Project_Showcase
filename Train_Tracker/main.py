from bs4 import BeautifulSoup
import requests
from datetime import datetime

def GetTrainTimesForTravel(Start,End,Time):
	"""GetTrainTimes(StationCode) will return live departure board"""
	def get_webCode(url):
		return BeautifulSoup(requests.get(url).text,features="html.parser")

	def DelayScanner(PossiblyDelays):
		Checked = ["On time","delayed","Cancelled ","late"]
		for Keyword in Checked:
			if Keyword in PossiblyDelays:
				return Keyword
		return "Delayed"
	html=list(get_webCode("https://ojp.nationalrail.co.uk/service/timesandfares/{}/{}/today/{}/dep".format(Start,End,Time)).findAll("td"))
	Trains = []
	print(html)
	for i in range(0,len(html)-4,5):
		OneTrain = [str(html[0+i]).strip("<td class=\"status status-minor-delay>\"/ \n"),str(html[1+i]).strip("<td class=\"destination\">\n\n\xa0\n\n</'"),DelayScanner(html[2+i]),str(html[3+i]).strip("<td></td>")]
		Trains.append(OneTrain)

	##return Trains


#print(GetTrainTimesForTravel("CBG", "KGX", 1500))
