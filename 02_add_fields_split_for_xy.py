
#add 2 new fields (lat, lng) (similar to loop above and then use split (( for x and then , for y

import urllib2
import json
import csv
import sys, re, time
import pandas as pd
import glob
import random

with open('all_shows_working.csv', 'r') as csvinput:
	with open('all_shows_working_lat.csv', 'w') as csvoutput:
		writer  = csv.writer(csvoutput, lineterminator='\n')
		reader = csv.reader(csvinput)

		all = []
		row = next(reader)
		row.append('lat')
		all.append(row)

		cnt_cols = len(row)
		z = cnt_cols

		for row in reader:

			try:
				lat = row[z-2].split('(', 2)[2].split(',',1)[0]
				lat = float(lat) + 0.0001*random.randint(1, 50)
				row.append(lat)
				all.append(row)

			except:
				lat = 0 + 0.0001*random.randint(1, 50)
				row.append(lat)
				all.append(row)


		writer.writerows(all)


with open('all_shows_working_lat.csv', 'r') as csvinput:
	with open('all_shows_working_lat_lng.csv', 'w') as csvoutput:
		writer  = csv.writer(csvoutput, lineterminator='\n')
		reader = csv.reader(csvinput)

		all = []
		row = next(reader)
		row.append('lng')
		all.append(row)

		cnt_cols = len(row)
		z = cnt_cols

		for row in reader:

			try:
				lng = row[z-3].split('(', 2)[2].split(',',1)[1].strip(')').strip(' ')
				lng = float(lng) + 0.0001*random.randint(1, 50)
				row.append(lng)
				all.append(row)

			except:
				lng = 0 + 0.0001*random.randint(1, 50)
				row.append(lng)
				all.append(row)


		writer.writerows(all)