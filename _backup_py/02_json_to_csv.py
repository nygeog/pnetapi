import urllib2
import json
import csv
import sys, re, time

pauser = 2

dirloc = "/Users/danielmsheehan/GitHub/pnetapi/"

#"https://api.phish.net/api.js?api=2.0&format=json&method=pnet.shows.query&year=2013&artist=1&apikey=7C7EADF07CC403838696"

preurl = "https://api.phish.net/api.js?api=2.0&format=json&method=pnet.shows.query&"
yearqu = "year="
midurl = "&artist=1&apikey="
apikey = '7C7EADF07CC403838696'

for year in range(1983,2014):
	url = preurl + yearqu + str(year) + midurl + apikey
	print url
	# data = urllib2.urlopen(url).read()
	# data = json.loads(data)
	# fname = dirloc + "shows_"+str(year)+".csv"
	# fjname = dirloc + "shows_"+str(year)+".json"
	# print data

	# with open(fjname, 'w') as outfile:
	# 	json.dump(data, outfile)

	# # with open(fname,'wb') as outf:
	# #  	outcsv = csv.writer(outf)
	# # 	outcsv.writerows((data))
	# #  	time.sleep( pauser )

	

	with open("checkins_mini_out.csv", "wb") as out_file:
		writer = csv.writer(out_file)
		the_url = url
		response = urllib2.urlopen(the_url)
		data = json.load(response)
		nam_return = data[1]["showyear"]
		the_info = nam_return	
		print the_info	
		try:

		 	outputRow = [nam_return]
		 	writer.writerow(outputRow)
		except:
		 	print "yo - I'm a weird address"
