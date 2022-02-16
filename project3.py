import pathlib; 
import urllib.request;
import re; 

file = pathlib.Path("./http_access_log.txt")
if file.exists ():
    print ("Loading")
else:
    print ("Download is starting")
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, "./http_access_log.txt")
          			      
apr = 0; may = 0; jun = 0; 			
jul = 0; aug = 0; sep = 0; oct95 = 0;

with open("./http_access_log.txt") as s:				
	for line in s:								
		if re.search('(/Apr/)', line):
				apr+=1
		if re.search('(/May/)', line):
				may+=1
		if re.search('(/Jun/)', line):
				jun+=1
		if re.search('(/Jul/)', line):
				jul+=1
		if re.search('(/Aug/)', line):
				aug+=1
		if re.search('(/Sep/)', line):
				sep+=1
		if re.search('(/Oct/1995)', line):				
				oct95+=1
				
print("Total requests made in last 6 months is?:", apr + may + jun + jul + aug + sep + oct95)
requests = len(open("./http_access_log.txt").readlines())
print('Total requests were made in the time period is?:', requests)
