import time, sys
import progressbar 

def progress_bar():

	bar = progressbar.ProgressBar(widgets=[
    	'Fetching Tweets: ',
    	progressbar.Bar(),
    	' (', progressbar.Timer(), ') ',
	])  
	for i in bar(range(50)):
		time.sleep(0.5)


	