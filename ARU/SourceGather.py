import requests
from bs4 import BeautifulSoup
class ITDgree():
	def ARUWebsite():
		JobsAtAru = []

		def get_webCode(url):
			return BeautifulSoup(requests.get(url).text,features="html.parser")

		def Filter(JobsAtAru):
			for eachJob in JobsAtAru:
				if "Digital and Technology" in eachJob:
					return True
			return False

		ARULink= get_webCode("https://avlive.apprenticeships.org.uk/remote/28b41d357d0a76a7b7566454f444c510").findAll("strong")
		for Job in ARULink:
			JobsAtAru.append(str(Job).strip("\r\n               <strong> </strong>",))

		if Filter(JobsAtAru):
			return ["Jobs Found",JobsAtAru]
		else:
			return ["No Jobs Found",JobsAtAru]

	def CleanPrintOut():
		CompletePrintOut = []
		ARUWebsiteData = ITDgree.ARUWebsite()
		CompletePrintOut.append("-=-=Anglia Ruskin Uni Apprenticeships=-=-\n There are {0}.\n\n Current Vacancies:".format(ARUWebsiteData[0]))
		for JobTitle in ARUWebsiteData[1]:
			CompletePrintOut.append("    ~ {}".format(JobTitle))
		return CompletePrintOut

if __name__ == '__main__':
	for line in ITDgree.CleanPrintOut():
		print(line)