import h5py


if __name__=='__main__':
	#Appending sentences to a list.
	firstList = []
	firstList.append('This is a sentence.')	
	firstList.append('But is this a sentence?')	
	firstList.append("Is NJIT's REU more than is horrible dorm management?")	
	firstList.append(1)
	firstList.append((1,2,3,4,5,))

	#Creating entries in a Python dictionary.
	firstDict = {}
	firstDict['Scientist Name'] = 'Matthew B. Cooper'
	firstDict['Degree'] = 'PhD'
	firstDict['Year Earned'] = 2023
	firstDict['Specialty Keywords'] = ['Space Plasma Thermodynamics',\
																		'Thermospheric Neutral Measurement',
																		'Drift-Mirror Instability']

	#Opening an hdf5 file type
	hf = h5py.File('firstFile.h5','w')
	print(hf.keys())
	dataset1 = [0,1,2,3,4]
	hf.create_dataset('dataset1',data=dataset1)
	print(hf['dataset1'])
	print(hf['dataset1'][()])
	hf.close()	
	
	#Creating an instrument dictionary
	hf = h5py.File('InstrumentFile.h5','r')
	print(hf.keys())
	secondDict = {'Instrument Name':'RBSPICE',\
								'Instrument Type':'Particle Detector',\
								'Energy Channels':hf['FPDU_Energy'][()]}	


