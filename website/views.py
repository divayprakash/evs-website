from django.shortcuts import render,get_object_or_404
import getDataAV,getDataCL,getDataPB,getDataMM,getDataRKP
from django.http import HttpResponse
from .models import Area,Pollutants

def index(request):

    return render(request,'website/index.html')


def pollutionInDelhi(request):

    return render(request,'website/page1.html')

def IIITD(request):

    return render(request,'website/page2.html')

def profile(request):

    return render(request,'website/page3.html')

def issue(request):

    return render(request,'website/page4.html')

def AnandVihar(request):
    DATA=getDataAV.DATA
    a=Area.objects.get(pk=1)
    for data in DATA:
        a.pollutants_set.create(param=str(data[0]),date=str(data[1]),time=str(data[2]), concen=str(data[3]), standard=str(data[4]))
        print str(data[2])
    L=a.pollutants_set.all()
    List=L[len(L)-10:len(L)-1]
    cont={'List':List,}
    context={'DATA':DATA,}
    return render(request,'website/data.html',cont)


def MandirMarg(request):
    DATA=getDataMM.DATA
    a=Area.objects.get(pk=2)
    for data in DATA:
        a.pollutants_set.create(param=str(data[0]),date=str(data[1]),time=str(data[2]), concen=str(data[3]), standard=str(data[4]))
        print data[2]
    L=a.pollutants_set.all()
    List=L[len(L)-10:len(L)-1]
    cont={'List':List,}
    context={'DATA':DATA,};
    return render(request,'website/data.html',cont)


def RKPuram(request):
    DATA = getDataRKP.DATA
    a = Area.objects.get(pk=1)
    for data in DATA:
        a.pollutants_set.create(param=str(data[0]), date=str(data[1]), time=str(data[2]), concen=str(data[3]),
                                standard=str(data[4]))
        print str(data[2])
    L = a.pollutants_set.all()
    List = L[len(L) - 10:len(L) - 1]
    cont = {'List': List,}
    context = {'DATA': DATA,}
    return render(request, 'website/data.html', cont)


def PunjabiBagh(request):
    DATA = getDataPB.DATA
    a = Area.objects.get(pk=1)
    for data in DATA:
        a.pollutants_set.create(param=str(data[0]), date=str(data[1]), time=str(data[2]), concen=str(data[3]),standard=str(data[4]))
        print str(data[2])
    L = a.pollutants_set.all()
    List = L[len(L) - 10:len(L) - 1]
    cont = {'List': List,}
    context = {'DATA': DATA,}
    return render(request, 'website/data.html', cont)


def CivilLines(request):
    DATA=getDataCL.DATA
    a=Area.objects.get(pk=3)
    for data in DATA:
        a.pollutants_set.create(param=str(data[0]), date=str(data[1]), time=str(data[2]), concen=str(data[3]),
                                standard=str(data[4]))
        print data[0], " addded into database"
    L = a.pollutants_set.all()
    List = L[len(L)-10:len(L)-1]
    cont = {'List': List,}
    context={'DATA':DATA,};
    return render(request,'website/data.html',cont)