import random

def GenQuestion():
	IndexReference = [20,12],[30,23],[40,36],[50,53],[60,73],[70,96]
	RandomGen = [random.randint(1,3),random.randint(1,6),random.randint(1,50),random.randint(1,100),] 
	if RandomGen[0] == 1:
		return ["What is the Stopping distance at {}?".format(IndexReference[RandomGen[1]-1][0]),["A:{}".format(IndexReference[RandomGen[1]-1][1]),"B:{}".format(RandomGen[2]),"C:{}".format(RandomGen[3])],"a"]
	if RandomGen[0] == 2:
		return ["What is the Stopping distance at {}?".format(IndexReference[RandomGen[1]-1][0]),["A:{}".format(RandomGen[2]),"B:{}".format(IndexReference[RandomGen[1]-1][1]),"C:{}".format(RandomGen[3])],"b"]
	if RandomGen[0] == 3:
		return ["What is the Stopping distance at {}?".format(IndexReference[RandomGen[1]-1][0]),["A:{}".format(RandomGen[2]),"B:{}".format(RandomGen[3]),"C:{}".format(IndexReference[RandomGen[1]-1][1])],"c"]

def MakeAnArray():
	return [GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion(),GenQuestion()]

def AskQustion(Question,Number):
	print("\n{}) {}\n{}\n{}\n{}".format(Number+1,Question[0],Question[1][0],Question[1][1],Question[1][2]))
	for i in Question[1]:
		if input("=").lower() == Question[2]:
			print("\nWell Done Question Correct!")
			return True
		else:
			print("\nSorry that's wrong the awnser is {}".format(Question[2]))
			return False

def TestDo(Questions):
	Score = 0
	for num,Question in enumerate(Questions):
		Check = AskQustion(Question,num)
		if Check == True:
			Score+= 1
	return Score

print("Well Done you scored: {}".format(TestDo(MakeAnArray())))

