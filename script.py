#BEER_NAME_GENERATOR

from datetime import datetime
import random

NUMBER_OF_NAMES = 100 #change this value for more outputs

for x in range(NUMBER_OF_NAMES):

	paint = file('_assets/paint.txt').readlines()
	suffix = file('_assets/suffix.txt').readlines()
	abv1 = file('_assets/abv1.txt').readlines()
	abv2= file('_assets/abv2.txt').readlines()

	#include fake ABV content
	#writeme = "%s %s // %s.%s%% ABV\n" % (random.choice(paint).rstrip(), random.choice(suffix).rstrip(), random.choice(abv1).rstrip(), random.choice(abv2).rstrip() )

	writeme = "%s %s \n" % (random.choice(paint).rstrip(), random.choice(suffix).rstrip(), )

	with open("tweet_" + datetime.now().strftime("%H:%M:%S").replace(':','.') + ".txt",'a') as output:
	    output.write(writeme)
	

