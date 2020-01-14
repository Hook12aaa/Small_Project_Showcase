
QuestionsComputing = ["Is a \"HDD\" a backing stoage? ",["A: Yes","B: No"],151],["Which Statment is ture about GUI?",["A: Hard to learn","B: Is the easiest to learn","C:Can be used for telephone exchanges"],152],["Can Open Source Software be privately owned",["A: True","A: False"],151,["What Operating System would an airplane use?",["A: Realtime","B: Single User","C: Multi-Tasking"],151]]
QuestionsICT= ["When did the data protection act come out?",["A:1999","B:1998","C:2001"],152],["What is Classifed Data?",["A:Legally Private Data","B:All Data held by a public coperation","C: Data reserved for ageneies"],151]
def AskQustion(Question,Number):
	print("\n{}) {}".format(Number,Question[0]))
	for i in Question[1]:
		print(i)
	if input("=").lower() == chr(Question[2]- 54):
		print("\nWell Done Question Correct!")
		return True
	else:
		print("\nSorry that's wrong the awnser is {}".format(chr(Question[2]-54)))
		return False

def TestDo(Questions):
	Score = 0
	for num,Question in enumerate(Questions):
		Check = AskQustion(Question,num)
		if Check == True:
			Score+= 1
	return Score

print("Well Done you scored: {}".format(TestDo(QuestionsICT)))

#["",["A:","B","C"]]


