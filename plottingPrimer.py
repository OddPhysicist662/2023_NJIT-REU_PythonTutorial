import datetime as dt
import numpy as np
import matplotlib.dates as mdates
import pandas as pd

if __name__=='__main__':
	'''
	Hard to make a plot without data.  This data is a geomagnetic index (Dst), 
	which is derived from ground-based magnetometer data and, from the classical
	perspective, indicates how much material is present inside the Earth's ring 
	current.  I'm using the pandas library to import the csv.  Pandas is a very 
	powerful tool for importing, sorting, repackaging, and exporting data.  I 
	don't use it in my normal workflows, but the man who taught me Python 
	involves it in most of his code infrastructure.  Since my csv has headers,
	Pandas can sort it into different datasets automatically.
	'''
	
	#Read in the code into a 'Pandas dataframe'
	df = pd.read_csv('Dst_Year.csv')
	print(df.keys())
		
	#In Python, objects such as dataframes have 'methods' attached to them, i.e.
	#the values method' of the dataframe, df, allows me to pull the values from
	#a particular column into a Python variable 
	epochs = df['Epoch'].values
	dst = df['Dst'].values
	
	print(type(epochs[0]))
	print(epochs[-1])
#	print(type(dst[-1]))

	newEpochs = []
	for epoch in epochs:
		newDate = dt.datetime.strptime(epoch,'%Y-%m-%d %H:%M:%S')
		newEpochs.append(newDate)	
	print(type(newEpochs[0]))

	'''
	The goal of a plot is to show information: maybe to yourself, but 
	in science others will likely want/need to see it as well to see if they 
	agree with your conclusions.  Plots for yourself are one thing; let's 
	focus on plots to share with others.  If other people can't read the labels 
	of your axes or the numbers on your tickmarks, the plot is failing its 
	primary goal of communicating information.
	'''

	#The easiest and quickest means of plotting in Python is using the pyplot 
	#library to draw the axes for you.  
	import matplotlib.pyplot as plt
	plt.plot(newEpochs,dst)
	plt.xlabel('Time',fontsize=14)
	plt.ylabel('Dst (nT)',fontsize=14)
	plt.xticks(fontsize=10,rotation=40)
	plt.yticks(fontsize=10)
	ax = plt.axes()
	ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
	plt.savefig('easyWay.png',bbox_inches='tight')
	plt.cla()

	#A slightly more complicated way of doing the same is by using the axes
	#object directly.  The variable 'ax' above is this object.  So that would 
	#look something like this.
	ax = plt.axes()
	ax.plot(newEpochs,dst)
	ax.set_xlabel('Time',fontsize=14)
	ax.set_ylabel('Dst (nT)',fontsize=14)
	ax.tick_params(axis='x',labelsize=10,rotation=40)
	ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
	ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
	plt.savefig('lessEasyWay.png',bbox_inches='tight')

	#Then, there is the most complicated method.  This allows for complete 
	#customization of axes location and sizes, but requires a lot of extra work
	#to make it readable for a general audience.  Lets use some of our 
	#Fabry-Perot measurements from Svalbard to illustrate.
		 
	#We use pyplot to create a Figure object.  This was done in the background 
	#for the two previous examples.
	fig = plt.figure(figsize=(15,13))

	'''
	This bit of code reads OUR image files into memory. May (probably) won't
	work if YOU have images you need to read in.  The data types may be 
	different, the images may not be the same size as our (512,512) image, 
	or the image file may be saved differently.  This is directly reading in the 
	binary data and then decoding it using numpy.
	'''
	fid = open('HODIMeasurement.img', 'rb')                                  
	data = np.fromfile(fid, '>u2')                                              
	fid.close()
	image = data[512:].reshape((512,512))
	
	#The first axes will be an image of the HODI 732 data.
	ax1 = fig.add_axes([.2,.25,.7,.7])
	ax1.xaxis.set_visible(False)
	ax1.yaxis.set_visible(False)
	im = ax1.imshow(image,cmap='jet',vmin=0,vmax=50000,zorder=0)                
	ax1.axvline(256)
	ax1.axhline(256)
	
	#Add an axes for the colorbar and make colorbar for the image
	axCbar = fig.add_axes([.86,.25,.03,.7])
	cbar = plt.colorbar(im, cax=axCbar,pad=.1)
	cbar.ax.tick_params(labelsize=20,rotation=-70)
	cbar.ax.set_ylabel('Counts',fontsize=25,rotation=270)
	cbar.ax.get_yaxis().labelpad = 30

	#Plot a slice of the image from the middle point of the x-axis
	ax2 = fig.add_axes([.05,.25,.2,.7])
	imageClip = image[:,256]
	ax2.plot(imageClip,np.arange(0,512,1))
	ax2.set_ylim(512,0)
	ax2.tick_params(axis='x',labelsize=20,rotation=-45)
	ax2.tick_params(axis='y',labelsize=20)
	ax2.set_ylabel('Y Pixel',fontsize=20)	

	#Plot a slice of the image from the middle point of the y-axis
	ax3 = fig.add_axes([.25,.05,.6025,.2])
	imageClip = image[256,:]
	ax3.plot(np.arange(0,512,1),imageClip)
	ax3.tick_params(axis='x',labelsize=20)
	ax3.tick_params(axis='y',labelsize=20,rotation=45)
	ax3.set_xlabel('X Pixel',fontsize=20)	
	ax3.yaxis.tick_right()
	plt.savefig('theHardWay.png',bbox_inches='tight')	
	fig.clf()

	'''
	This section plots the exact same thing as the previous, but I've used 
	a median filter to smooth the noise.	
	'''
	import scipy.ndimage as sciIm
	image = sciIm.median_filter(image,size=5,mode='reflect')
	#The first axes will be an image of the HODI 732 data.
	ax1 = fig.add_axes([.2,.25,.7,.7])
	ax1.xaxis.set_visible(False)
	ax1.yaxis.set_visible(False)
	im = ax1.imshow(image,cmap='jet',vmin=0,vmax=50000,zorder=0)                
	ax1.axvline(256)
	ax1.axhline(256)
	
	#Add an axes for the colorbar and make colorbar for the image
	axCbar = fig.add_axes([.86,.25,.05,.7])
	cbar = plt.colorbar(im, cax=axCbar)
	cbar.ax.tick_params(labelsize=20)

	#Plot a slice of the image from the middle point of the x-axis
	ax2 = fig.add_axes([.05,.25,.2,.7])
	imageClip = image[:,256]
	ax2.plot(imageClip,np.arange(0,512,1))
	ax2.set_ylim(512,0)
	ax2.tick_params(axis='x',labelsize=20,rotation=-90)
	ax2.tick_params(axis='y',labelsize=20)
	ax2.set_ylabel('Y Pixel',fontsize=20)	

	#Plot a slice of the image from the middle point of the y-axis
	ax3 = fig.add_axes([.25,.05,.6025,.2])
	imageClip = image[256,:]
	ax3.plot(np.arange(0,512,1),imageClip)
	ax3.tick_params(axis='x',labelsize=20)
	ax3.tick_params(axis='y',labelsize=20)
	ax3.set_xlabel('X Pixel',fontsize=20)	
	ax3.yaxis.tick_right()
	plt.savefig('theHardWayClean.png',bbox_inches='tight')	
	fig.clf()











