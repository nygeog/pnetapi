import urllib2
import json
import csv
import sys, re, time
import pandas as pd
import glob
from geopy.geocoders import GoogleV3

geolocator = GoogleV3()

pauser = .1

preurl = "https://api.phish.net/api.js?api=2.0&format=json&method=pnet.shows.query&"
yearqu = "year="
midurl = "&artist=1&apikey="
apikey = '7C7EADF07CC403838696'

years_active = [
'1983',
'1984',
'1985',
'1986',
'1987',
'1988',
'1989',
'1990',
'1991',
'1992',
'1993',
'1994',
'1995',
'1996',
'1997',
'1998',
'1999',
'2000',
'2001',
'2002',
'2003',
'2004',
'2009',
'2010',
'2011',
'2012',
'2013']

for year in years_active:
	url = preurl + yearqu + str(year) + midurl + apikey
	print url
	d = pd.read_json(url)
	d.to_csv("shows_"+str(year)+".csv", sep=',',index=False)

all_csvs = glob.glob("*.csv")

print all_csvs

df_list = []

i = 0
for allcsvs in all_csvs:
	df = pd.read_csv(allcsvs, header=0)
	df_list.append(df)
	i += 1
	print i

df = pd.concat(df_list)
df = df.sort_index(axis=1)

df.to_csv('all_shows.csv', sep=',', index=False)

with open('all_shows.csv', 'r') as csvinput:
	with open('all_shows_working.csv', 'w') as csvoutput:
		writer  = csv.writer(csvoutput, lineterminator='\n')
		reader = csv.reader(csvinput)

		all = []
		row = next(reader)
		row.append('cords')
		all.append(row)

		cnt_cols = len(row)
		z = cnt_cols

		for row in reader:
			exp = str(row[z-3]) + ', ' + str(row[z-13]) + ', ' + str(row[z-4]) + ', ' + str(row[z-12])
			#print exp
			try:
				cordout = geolocator.geocode(exp)
				#cordout = exp
				print cordout
				row.append(cordout)
				all.append(row)
			except:
				row.append('missing')
				all.append(row)
				print 'missing'

			time.sleep(pauser)
			i += 1
			print i

		writer.writerows(all)
