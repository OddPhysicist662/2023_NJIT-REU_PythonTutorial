
if __name__=='__main__':
	#Appending sentences to a list.
	firstList = []
	firstList.append('This is a sentence.')	
	firstList.append('But is this a sentence?')	
	firstList.append("Is NJIT's REU more than its dorm management?")	
	firstList.append(1)
	firstList.append((1,2,3,4,5,))
	for item in firstList:
		print(item)
	print()
	
	#Creating entries in a Python dictionary.
	firstDict = {}
	firstDict['Scientist Name'] = 'Matthew B. Cooper'
	firstDict['Degree'] = 'PhD'
	firstDict['Year Earned'] = 2023
	firstDict['Specialty Keywords'] = ['Space Plasma Thermodynamics',\
																		'Thermospheric Neutral Measurement',
																		'Drift-Mirror Instability']
	for key in firstDict.keys():
		print(key)
	
