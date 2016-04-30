
# Data of RK Puram
place='rkPuram'
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



RKP_aRKPonia=csv.writer(open("../data_files/RKP/RKP_aRKPonia.csv","a"))
RKP_benzene=csv.writer(open("../data_files/RKP/RKP_benzene.csv","a"))
RKP_Cmonoxide=csv.writer(open("../data_files/RKP/RKP_Cmonoxide.csv","a"))
RKP_Ndioxide=csv.writer(open("../data_files/RKP/RKP_Ndioxide.csv","a"))
RKP_Noxide=csv.writer(open("../data_files/RKP/RKP_Noxide.csv","a"))
RKP_oxidesN=csv.writer(open("../data_files/RKP/RKP_oxidesN.csv","a"))
RKP_ozone=csv.writer(open("../data_files/RKP/RKP_ozone.csv","a"))
RKP_xylene=csv.writer(open("../data_files/RKP/RKP_xylene.csv","a"))
RKP_Sdioxide=csv.writer(open("../data_files/RKP/RKP_Sdioxide.csv","a"))
RKP_toluene=csv.writer(open("../data_files/RKP/RKP_toluene.csv","a"))
RKP_Bpressure=csv.writer(open("../data_files/RKP/RKP_pressure.csv","a"))
RKP_temp=csv.writer(open("../data_files/RKP/RKP_temp.csv","a"))
RKP_humidity=csv.writer(open("../data_files/RKP/RKP_humidity.csv","a"))
RKP_PM10=csv.writer(open("../data_files/RKP/RKP_PM10.csv","a"))
RKP_PM25=csv.writer(open("../data_files/RKP/RKP_PM25.csv","a"))
RKP_Sradiation=csv.writer(open("../data_files/RKP/RKP_Sradiation.csv","a"))
RKP_VWS=csv.writer(open("../data_files/RKP/RKP_VWS.csv","a"))
RKP_HWS=csv.writer(open("../data_files/RKP/RKP_HWS.csv","a"))
RKP_direction=csv.writer(open("../data_files/RKP/RKP_direction.csv","a"))
#RKP_speed=csv.writer(open("../data_files/RKP/RKP_speed.csv","a"))
exportFrom='http://www.dpccairdata.com/dpccairdata/display/'+place+'View15MinData.php'
res=requests.get(exportFrom)
try:
	res.raise_for_status()
	RKPuster=bs4.BeautifulSoup(res.text,"lxml")
	E=RKPuster.select('td')
	#print len(E)
	#print E[44].getText()
	DATA=[]
	appendInFile(20,27,RKP_aRKPonia)
	appendInFile(27,34,RKP_benzene)
	appendInFile(34,41,RKP_Cmonoxide)
	appendInFile(41,48,RKP_Ndioxide)
	appendInFile(48,55,RKP_Noxide)
	appendInFile(55,62,RKP_oxidesN)
	appendInFile(62,69,RKP_ozone)
	appendInFile(69,76,RKP_xylene)
	appendInFile(76,83,RKP_Sdioxide)
	appendInFile(83,90,RKP_toluene)
	print E[107].getText()
	appendInFile(100,107,RKP_temp)
	appendInFile(107,114,RKP_Bpressure)
	appendInFile(114,121,RKP_PM10)
	appendInFile(121,128,RKP_PM25)
	appendInFile(128,135,RKP_humidity)
	appendInFile(135,142,RKP_Sradiation)
	appendInFile(142,149,RKP_VWS)
	appendInFile(149,156,RKP_HWS)
	appendInFile(156,163,RKP_direction)
	
except Exception as e:
	print "Something went wrong ",(e)
