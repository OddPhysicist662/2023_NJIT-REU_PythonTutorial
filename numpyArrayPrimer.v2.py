import numpy as np
import h5py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

if __name__=='__main__':
	df = pd.read_csv('Dst_Year.csv')
		
	epochs = df['Epoch'].values
	dst = df['Dst'].values

	newEpochs = []
	for epoch in epochs:
		newDate = dt.datetime.strptime(epoch,'%Y-%m-%d %H:%M:%S')
		newEpochs.append(newDate)	
	newEpochs = np.array(newEpochs)

	#Using argwhere to select entries
	reducInds = np.argwhere(dst >0)
	epochsReduc = newEpochs[reducInds][:,0]
	dstReduc = dst[reducInds][:,0]
	plt.plot(epochsReduc,dstReduc,color='blue')

	#Using argwhere with multiple conditions
	reducInds = np.argwhere((dst <= 0) & (dst >= -50))
	epochsReduc = newEpochs[reducInds][:,0]
	dstReduc = dst[reducInds][:,0]
	plt.plot(epochsReduc,dstReduc,color='green')

	#Making the plot pretty
	plt.xlabel('Time',fontsize=14)
	plt.ylabel('Dst (nT)',fontsize=14)
	plt.xticks(fontsize=14,rotation=40)
	plt.yticks(fontsize=14)
	plt.tight_layout()
	ax = plt.axes()
	ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
	plt.savefig('plottingPrimerReducInds.png')	

	#Masking Bad Values
	hf = h5py.File('InstrumentFile.h5','r')

	flux = hf['FPDU']
	meas = flux[-18,:,:]
	print(meas)
	print(np.mean(meas))

	measMasked = np.ma.masked_where(meas<0,meas)

	print(np.mean(measMasked))
