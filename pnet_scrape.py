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
	data = urllib2.urlopen(url).read()
	data = json.loads(data)
	fname = dirloc + "shows_"+str(year)+".csv"
	fjname = dirloc + "shows_"+str(year)+".json"
	print data

	with open(fjname, 'w') as outfile:
		json.dump(data, outfile)

	# with open(fname,'wb') as outf:
	#  	outcsv = csv.writer(outf)
	# 	outcsv.writerows((data))
	#  	time.sleep( pauser )

	# modify from foursquare scraper 

	with open("checkins_mini_out.csv", "wb") as out_file:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        writer = csv.writer(out_file)
        for row in reader:

                try:
                        venue_id = row[1]
                        ts_epoch = float(row[0])
                        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts_epoch))
                        the_url = 'https://api.foursquare.com/v2/venues/' + str(venue_id) + '?oauth_token=DKMQRQ5G33P5B1XQIHBJRPPVS2QXJ1NX4US0CWOEFEOJDLIK&v=20131021'
                        response = urllib2.urlopen(the_url)
                        data = json.load(response)
                        nam_return = data["response"]["venue"]["name"]
                        adr_return = data["response"]["venue"]["location"]["address"]
                        web_return = data["response"]["venue"]["shortUrl"]
                        chk_return = data["response"]["venue"]["stats"] ["checkinsCount"]
                        lat_return = data["response"]["venue"]["location"]["lat"]
                        lng_return = data["response"]["venue"]["location"]["lng"]
                        the_info = venue_id + ',' + ts + ',' + nam_return + ',' + adr_return + ',' + str(chk_return)  + ',' + web_return  + ',' + str(lat_return) + ',' + str(lng_return)
                        print the_info
                        outputRow = [venue_id, ts, nam_return, adr_return, web_return, chk_return, lat_return, lng_return]
                        writer.writerow(outputRow)
                except:
                        print "yo - I'm a weird address"