from datetime import datetime
from time import sleep

endProg = False 

def getStartTime():
	return datetime.now()

def getEndTime():
	return datetime.now()

def getHMSus(t):
	return "{} : {: 0>2} : {}".format(t.hour,t.minute,t.second + t.microsecond /1000000)

def timeStarted(startT):
	print("start  : {}".format(getHMSus(startT)))

def timeTaken(startT,endT):
	totalT = endT - startT
	print("end : {} \n Time taken: {}".format(getHMSus(endT),totalT))

def bigO1():
	maxIt = int(input("enter the nmber of interations: "))
	st = getStartTime()
	timeStarted(st)
	print(maxIt)
	et = getEndTime()
	timeTaken(st,et)

def bigON():
	maxIt = int(input)
	st = getStartTime()
	timeStarted(st)
	for i in range(maxIt):
		sleep(0.001)
		print(i)	
	et = getEndTime()
	timeTaken(st,et)


def bigOsquared():
	maxIt = int(input("enter the number of interations"))
	st = getStartTime()
	timeStarted(st)
	for i in range(maxIt):
		sleep(0.001)
		print(i)
		for j in range(maxIt):
			sleep(0.001)
			print(j)
	et = getEndTime()
	timeTaken(st,et)

def bigOpowerN():
	maxLen = int(input("enter number of passwordsL: "))
	pWords = []
	for i in range(maxLen):
		pWords.append(input("enter a random password of  {0} characters. \n" \
			"only use the first {0} letters of the " \
			" alphabet".format(maxLen)))
	loopcount = 0 
	st = getStartTime()
	timeStarted()
	print()
	for i in range(maxLen):
		for j in range(len(pWords[i])):
			sleep(0.001)
			asciVal = 97
			for k in range(len(pWords[i])):
				print("checking {} position: {}".format(pWords[i],j))
				print("checking for {}".format(chr(asciVal)))
				if pWords[i][j] == chr(asciVal):
					print("{} was found at position {}".format(chr(asciVal),j))
				asciVal += 1
				loopcount += 1
				print()	
			loopcount += 1
		loopcount += 1
	et = getEndTime()
	timeTaken(st,et)
		