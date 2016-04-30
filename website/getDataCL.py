
# Data of Civil lines
place='civilLines'
#filenames
import requests,bs4
import csv


def parser(fault):
	l=len(fault)
	i=l-1
	while(i>=0):
		if(fault[i]=="1" or fault[i]=="2"  or fault[i]=="4" or fault[i]=="5" or fault[i]=="6" or fault[i]=="7" or fault[i]=="8" or fault[i]=="9" or fault[i]=="0"):
			break
		else:
			i-=1
	return fault[:i+1]			

def appendInFile(start,end):
	i=start  
	while i<end:

		SET=[]
		param=E[i].getText()
		date=E[i+1].getText()
		time=E[i+2].getText()
		concen=parser(E[i+3].getText().strip())
		standard=parser(E[i+4].getText().strip())
		SET.append(param)
		SET.append(date)
		SET.append(time)
		SET.append(concen)
		SET.append(standard)
		print SET
		
		#filename.writerow(SET)
		#DATA.append(SET)
		i+=7


"""
cl_ammonia=csv.writer(open("../data_files/CL/cl_ammonia.csv","a"))
cl_benzene=csv.writer(open("../data_files/CL/cl_benzene.csv","a"))
cl_formal=csv.writer(open("../data_files/CL/cl_formal.csv","a"))
cl_mecury=csv.writer(open("../data_files/CL/cl_mecury.csv","a"))
cl_Ndioxide=csv.writer(open("../data_files/CL/cl_Ndioxide.csv","a"))
cl_Noxide=csv.writer(open("../data_files/CL/cl_Noxide.csv","a"))
cl_ozone=csv.writer(open("../data_files/CL/cl_ozone.csv","a"))
cl_xylene=csv.writer(open("../data_files/CL/cl_xylene.csv","a"))
cl_Sdioxide=csv.writer(open("../data_files/CL/cl_Sdioxide.csv","a"))
cl_toluene=csv.writer(open("../data_files/CL/cl_toluene.csv","a"))
cl_pressure=csv.writer(open("../data_files/CL/cl_pressure.csv","a"))
cl_temp=csv.writer(open("../data_files/CL/cl_temp.csv","a"))
cl_humidity=csv.writer(open("../data_files/CL/cl_humidity.csv","a"))
cl_PM10=csv.writer(open("../data_files/CL/cl_PM10.csv","a"))
cl_PM25=csv.writer(open("../data_files/CL/cl_PM25.csv","a"))
cl_direction=csv.writer(open("../data_files/CL/cl_direction.csv","a"))
cl_speed=csv.writer(open("../data_files/CL/cl_speed.csv","a"))"""
exportFrom='http://www.dpccairdata.com/dpccairdata/display/'+place+'View15MinData.php'
res=requests.get(exportFrom)
try:
	res.raise_for_status()
	cluster=bs4.BeautifulSoup(res.text,"lxml")
	E=cluster.select('td')
	#print len(E)
	#print E[20].getText()
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
	#print E[99].getText()
	# appendInFile(99,106)
	# appendInFile(106,113)
	# appendInFile(113,120)
	# appendInFile(120,127)
	# appendInFile(127,134)
	# appendInFile(134,141)
	# appendInFile(141,148)
except Exception as e:
	print "Something went wrong ",(e)