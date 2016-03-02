
# Data of Civil lines
place='pb'
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



def appendInFile(start,end,filename):
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
		#SET.append(param)
		SET.append(date)
		SET.append(time)
		SET.append(concen)
		SET.append(standard)
		#print SET
		
		filename.writerow(SET)
		DATA.append(SET)
		i+=7



PB_ammonia=csv.writer(open("../data_files/PB/PB_ammonia.csv","a"))
PB_benzene=csv.writer(open("../data_files/PB/PB_benzene.csv","a"))
PB_Cmonoxide=csv.writer(open("../data_files/PB/PB_Cmonoxide.csv","a"))
PB_Ndioxide=csv.writer(open("../data_files/PB/PB_Ndioxide.csv","a"))
PB_Noxide=csv.writer(open("../data_files/PB/PB_Noxide.csv","a"))
PB_oxidesN=csv.writer(open("../data_files/PB/PB_oxidesN.csv","a"))
PB_ozone=csv.writer(open("../data_files/PB/PB_ozone.csv","a"))
PB_xylene=csv.writer(open("../data_files/PB/PB_xylene.csv","a"))
PB_Sdioxide=csv.writer(open("../data_files/PB/PB_Sdioxide.csv","a"))
PB_toluene=csv.writer(open("../data_files/PB/PB_toluene.csv","a"))
PB_Bpressure=csv.writer(open("../data_files/PB/PB_pressure.csv","a"))
PB_temp=csv.writer(open("../data_files/PB/PB_temp.csv","a"))
PB_humidity=csv.writer(open("../data_files/PB/PB_humidity.csv","a"))
PB_PM10=csv.writer(open("../data_files/PB/PB_PM10.csv","a"))
PB_PM25=csv.writer(open("../data_files/PB/PB_PM25.csv","a"))
PB_Sradiation=csv.writer(open("../data_files/PB/PB_Sradiation.csv","a"))
PB_VWS=csv.writer(open("../data_files/PB/PB_VWS.csv","a"))
PB_HWS=csv.writer(open("../data_files/PB/PB_HWS.csv","a"))
PB_direction=csv.writer(open("../data_files/PB/PB_direction.csv","a"))
#PB_speed=csv.writer(open("../data_files/PB/PB_speed.csv","a"))
exportFrom='http://www.dpccairdata.com/dpccairdata/display/'+place+'View15MinData.php'
res=requests.get(exportFrom)
try:
	res.raise_for_status()
	PBuster=bs4.BeautifulSoup(res.text,"lxml")
	E=PBuster.select('td')
	#print len(E)
	#print E[44].getText()
	DATA=[]
	appendInFile(20,27,PB_ammonia)
	appendInFile(27,34,PB_benzene)
	appendInFile(34,41,PB_Cmonoxide)
	appendInFile(41,48,PB_Ndioxide)
	appendInFile(48,55,PB_Noxide)
	appendInFile(55,62,PB_oxidesN)
	appendInFile(62,69,PB_ozone)
	appendInFile(69,76,PB_xylene)
	appendInFile(76,83,PB_Sdioxide)
	appendInFile(83,90,PB_toluene)
	print E[107].getText()
	appendInFile(100,107,PB_temp)
	appendInFile(107,114,PB_Bpressure)
	appendInFile(114,121,PB_PM10)
	appendInFile(121,128,PB_PM25)
	appendInFile(128,135,PB_humidity)
	appendInFile(135,142,PB_Sradiation)
	appendInFile(142,149,PB_VWS)
	appendInFile(149,156,PB_HWS)
	appendInFile(156,163,PB_direction)
	
except Exception as e:
	print "Something went wrong ",(e)
