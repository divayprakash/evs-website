from django.shortcuts import render,get_object_or_404
import getDataAV
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
    #a=Area.objects.get(pk=1)
    for data in DATA:
        #a.pollutants_set.create(param=data[0],date=data[1],time=data[2], concen=data[3], standard=data[4])
        print str(data[2])+"H"
    context={'DATA':DATA,};
    return render(request,'website/data.html',context)

# def AnandVihar(request):
#     DATA=getDataAV.DATA
#     a=Area.objects.get(pk=1)
#     for data in DATA:
#         a.pollutants_set.create(param=data[0],date=data[1],time=data[2], concen=data[3], standard=data[4])
#         print data[0], " addded into database"
#     context={'DATA':DATA,};
#     return render(request,'website/data.html',context)