import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

if __name__=='__main__':
	df = pd.read_csv('Dst_Year.csv')
	print(df.keys())
		
	epochs = df['Epoch'].values
	dst = df['Dst'].values
	
	print(epochs[-1])
#	print(type(dst[-1]))

	newEpochs = []
	for epoch in epochs:
		newDate = dt.datetime.strptime(epoch,'%Y-%m-%d %H:%M:%S')
		print(type(newDate))
		newEpochs.append(newDate)	

	plt.plot(newEpochs,dst)
	plt.xlabel('Time',fontsize=14)
	plt.ylabel('Dst (nT)',fontsize=14)
	plt.xticks(fontsize=14,rotation=40)
	plt.yticks(fontsize=14)
	plt.tight_layout()
	ax = plt.axes()
	ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
	plt.savefig('plottingPrimer3.png')	
