import requests
from bs4 import BeautifulSoup


class UkTrainLiveDeparture():
	""" Use function GetTrainTimes made by Anton Chepaldin """
	def GetTrainTimes(Location):
		"""GetTrainTimes(StationCode) will return live departure board"""
		def get_webCode(url):
			return BeautifulSoup(requests.get(url).text,features="html.parser")

		def DelayScanner(PossiblyDelays):
			Checked = ["On time","delayed","Cancelled ","late"]
			for Keyword in Checked:
				if Keyword in PossiblyDelays:
					return Keyword
			return "Delayed"

		html=list(get_webCode("https://ojp.nationalrail.co.uk/service/ldbboard/dep/"+Location.upper()).findAll("td"))
		Trains = []

		for i in range(0,len(html)-4,5):
			OneTrain = [str(html[0+i]).strip("<td class=\"status status-minor-delay>\"/ \n"),str(html[1+i]).strip("<td class=\"destination\">\n\n\xa0\n\n</'"),DelayScanner(html[2+i]),str(html[3+i]).strip("<td></td>")]
			Trains.append(OneTrain)

		return Trains

	def TrainServiceOkayOrBad(Station):	
		"""This compares the given data set provided by the GetTrainTimes() into how many trains have issues compared to on time trains"""
		DataRecorded = [["No Problems",0,""],["Issues",0,""]]
		PossibleIssuesIndex = ["late","delayed","cancelled "]
		for iteam in UkTrainLiveDeparture.GetTrainTimes(Station):
			if iteam[2].lower() == "on time":
				DataRecorded[0][1]+= 1
				DataRecorded[0][2]= iteam

			for DifferentIssues in PossibleIssuesIndex:
				if DifferentIssues == iteam[2].lower():
					DataRecorded[1][1]+= 1
					DataRecorded[1][2]= iteam
		return DataRecorded

	def


if __name__ == '__main__':
	def PrintTrainList(TrainList):
		for num,iteam in enumerate(TrainList):
			print("({})=-{} {} {}".format(TrainList[num][0],TrainList[num][1],TrainList[num][2],TrainList[num][3]))
	
	def PrintTrainIssues(TrainServiceUpdate):
		print(""" ----=Train Service Update=----

     	On Time = {0}/{1}
		Issues  = {2}/{1}

Direction Of Possible Train Delay = {3}
-------------------------------
		""".format(TrainServiceUpdate[0][1],TrainServiceUpdate[0][1]+TrainServiceUpdate[1][1],TrainServiceUpdate[1][1],TrainServiceUpdate[1][2][1]))
	PrintTrainIssues(UkTrainLiveDeparture.TrainServiceOkayOrBad("Ely"))
	PrintTrainList(UkTrainLiveDeparture.GetTrainTimes("Ely"))



