
# Data of Mandir Marg
place='mm'
#filenames
import requests,bs4
import csv


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
		SET.append(param)
		SET.append(date)
		SET.append(time)
		SET.append(concen)
		SET.append(standard)
		#print SET
		
		#filename.writerow(SET)
		DATA.append(SET)
		i+=7



# MM_ammonia=csv.writer(open("../data_files/MM/MM_ammonia.csv","a"))
# MM_benzene=csv.writer(open("../data_files/MM/MM_benzene.csv","a"))
# MM_Cmonoxide=csv.writer(open("../data_files/MM/MM_Cmonoxide.csv","a"))
# MM_Ndioxide=csv.writer(open("../data_files/MM/MM_Ndioxide.csv","a"))
# MM_Noxide=csv.writer(open("../data_files/MM/MM_Noxide.csv","a"))
# MM_oxidesN=csv.writer(open("../data_files/MM/MM_oxidesN.csv","a"))
# MM_ozone=csv.writer(open("../data_files/MM/MM_ozone.csv","a"))
# MM_xylene=csv.writer(open("../data_files/MM/MM_xylene.csv","a"))
# MM_Sdioxide=csv.writer(open("../data_files/MM/MM_Sdioxide.csv","a"))
# MM_toluene=csv.writer(open("../data_files/MM/MM_toluene.csv","a"))
# MM_Bpressure=csv.writer(open("../data_files/MM/MM_pressure.csv","a"))
# MM_temp=csv.writer(open("../data_files/MM/MM_temp.csv","a"))
# MM_humidity=csv.writer(open("../data_files/MM/MM_humidity.csv","a"))
# MM_PM10=csv.writer(open("../data_files/MM/MM_PM10.csv","a"))
# MM_PM25=csv.writer(open("../data_files/MM/MM_PM25.csv","a"))
# MM_Sradiation=csv.writer(open("../data_files/MM/MM_Sradiation.csv","a"))
# MM_VWS=csv.writer(open("../data_files/MM/MM_VWS.csv","a"))
# MM_HWS=csv.writer(open("../data_files/MM/MM_HWS.csv","a"))
# MM_direction=csv.writer(open("../data_files/MM/MM_direction.csv","a"))
#MM_speed=csv.writer(open("../data_files/MM/MM_speed.csv","a"))
exportFrom='http://www.dpccairdata.com/dpccairdata/display/'+place+'View15MinData.php'
res=requests.get(exportFrom)
try:
	res.raise_for_status()
	MMuster=bs4.BeautifulSoup(res.text,"lxml")
	E=MMuster.select('td')
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
	# print E[107].getText()
	# appendInFile(100,107,MM_temp)
	# appendInFile(107,114,MM_Bpressure)
	# appendInFile(114,121,MM_PM10)
	# appendInFile(121,128,MM_PM25)
	# appendInFile(128,135,MM_humidity)
	# appendInFile(135,142,MM_Sradiation)
	# appendInFile(142,149,MM_VWS)
	# appendInFile(149,156,MM_HWS)
	# appendInFile(156,163,MM_direction)
	#
except Exception as e:
	print "Something went wrong ",(e)
