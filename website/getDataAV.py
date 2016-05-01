import requests,bs4
# Data of Anand Vihar
place='av'


def parser(fault):
	#print "before ",fault
	l=len(fault)
	i=l-1
	while(i>=0):
		if(fault[i]=="1" or fault[i]=="2"  or fault[i]=="4" 
			or fault[i]=="5" or fault[i]=="6" or fault[i]=="7" 
			or fault[i]=="8" or fault[i]=="9" or fault[i]=="0"):
			break
		else:
			i-=1
	fault=fault[:i+1]
	#print "mid ",fault
	i=0
	while(i<len(fault)):
		if(fault[i]=="1" or fault[i]=="2"  or fault[i]=="3" or fault[i]=="4" or fault[i]=="5" or fault[i]=="6" or fault[i]=="7" or fault[i]=="8" or fault[i]=="9" or fault[i]=="0"):
			break
		else:
			i+=1
	fault=fault[i:]
	#print "after ",fault
	return fault



def appendInFile(start,end):
	i=start  
	while i<end:

		SET=[]
		param=E[i].getText()
		date=E[i+1].getText()
		time=E[i+2].getText()
		concen=parser(E[i+3].getText().strip())
		standard=parser(E[i+4].getText().strip())
		#print param
		#print date
		#print time
		#print concen
		#print standard
		SET.append(str(param))
		SET.append(str(date))
		SET.append(str(time))
		SET.append(str(concen))
		SET.append(str(standard))
		#print SET

		DATA.append(SET)
		i+=7

exportFrom='http://www.dpccairdata.com/dpccairdata/display/'+place+'View15MinData.php'
res=requests.get(exportFrom)


try:
	res.raise_for_status()
	AVuster=bs4.BeautifulSoup(res.text,"lxml")
	E=AVuster.select('td')
	#print len(E)
	#print E[44].getText()
	DATA=[]
	appendInFile(20,27)
	appendInFile(27,34)
	appendInFile(34,41)
	appendInFile(41,48)
	appendInFile(48,55)
	appendInFile(55,62)
	appendInFile(62,69)
	appendInFile(69,76)
	appendInFile(76,83)
	appendInFile(83,90)
	#print E[107].getText()
	# appendInFile(100,107,"temprature")
	# appendInFile(107,114,"Barometric pressure")
	# appendInFile(114,121,"PM10")
	# appendInFile(121,128,"PM25")
	# appendInFile(128,135,"humidity")
	# appendInFile(135,142,"Solar radiation")
	# appendInFile(142,149,"Vertical wind speed")
	# appendInFile(149,156,"Horizontal wind speed")
	# appendInFile(156,163,"Wind direction")


except Exception as e:
	print "[NOTE : WE ARE NOT ABLE TO CONNECT WITH SENSORS ]"
