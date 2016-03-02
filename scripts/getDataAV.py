
# Data of Anand Vihar
place='av'
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



AV_ammonia=csv.writer(open("../data_files/AV/AV_ammonia.csv","a"))
AV_benzene=csv.writer(open("../data_files/AV/AV_benzene.csv","a"))
AV_Cmonoxide=csv.writer(open("../data_files/AV/AV_Cmonoxide.csv","a"))
AV_Ndioxide=csv.writer(open("../data_files/AV/AV_Ndioxide.csv","a"))
AV_Noxide=csv.writer(open("../data_files/AV/AV_Noxide.csv","a"))
AV_oxidesN=csv.writer(open("../data_files/AV/AV_oxidesN.csv","a"))
AV_ozone=csv.writer(open("../data_files/AV/AV_ozone.csv","a"))
AV_xylene=csv.writer(open("../data_files/AV/AV_xylene.csv","a"))
AV_Sdioxide=csv.writer(open("../data_files/AV/AV_Sdioxide.csv","a"))
AV_toluene=csv.writer(open("../data_files/AV/AV_toluene.csv","a"))
AV_Bpressure=csv.writer(open("../data_files/AV/AV_pressure.csv","a"))
AV_temp=csv.writer(open("../data_files/AV/AV_temp.csv","a"))
AV_humidity=csv.writer(open("../data_files/AV/AV_humidity.csv","a"))
AV_PM10=csv.writer(open("../data_files/AV/AV_PM10.csv","a"))
AV_PM25=csv.writer(open("../data_files/AV/AV_PM25.csv","a"))
AV_Sradiation=csv.writer(open("../data_files/AV/AV_Sradiation.csv","a"))
AV_VWS=csv.writer(open("../data_files/AV/AV_VWS.csv","a"))
AV_HWS=csv.writer(open("../data_files/AV/AV_HWS.csv","a"))
AV_direction=csv.writer(open("../data_files/AV/AV_direction.csv","a"))
#AV_speed=csv.writer(open("../data_files/AV/AV_speed.csv","a"))
exportFrom='http://www.dpccairdata.com/dpccairdata/display/'+place+'View15MinData.php'
res=requests.get(exportFrom)
try:
	res.raise_for_status()
	AVuster=bs4.BeautifulSoup(res.text,"lxml")
	E=AVuster.select('td')
	#print len(E)
	#print E[44].getText()
	DATA=[]
	appendInFile(20,27,AV_ammonia)
	appendInFile(27,34,AV_benzene)
	appendInFile(34,41,AV_Cmonoxide)
	appendInFile(41,48,AV_Ndioxide)
	appendInFile(48,55,AV_Noxide)
	appendInFile(55,62,AV_oxidesN)
	appendInFile(62,69,AV_ozone)
	appendInFile(69,76,AV_xylene)
	appendInFile(76,83,AV_Sdioxide)
	appendInFile(83,90,AV_toluene)
	print E[107].getText()
	appendInFile(100,107,AV_temp)
	appendInFile(107,114,AV_Bpressure)
	appendInFile(114,121,AV_PM10)
	appendInFile(121,128,AV_PM25)
	appendInFile(128,135,AV_humidity)
	appendInFile(135,142,AV_Sradiation)
	appendInFile(142,149,AV_VWS)
	appendInFile(149,156,AV_HWS)
	appendInFile(156,163,AV_direction)
	
except Exception as e:
	print "Something went wrong ",(e)
