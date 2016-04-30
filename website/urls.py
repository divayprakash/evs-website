from django.conf.urls import url
from . import views

app_name='website'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^detail/$',views.pollutionInDelhi, name='pollutionInDelhi'),
    url(r'^IIITD/$', views.IIITD, name='IIITD'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^issue/$', views.issue, name='issue'),
    url(r'^detail/dataAnand/$', views.AnandVihar, name='AnandVihar'),
    url(r'^detail/dataMandir/$', views.MandirMarg, name='MandirMarg'),
    url(r'^detail/dataRKPuram/$', views.RKPuram, name='RKPuram'),
    url(r'^detail/dataPunjabi/$', views.PunjabiBagh, name='PunjabiBagh'),
    url(r'^detail/dataCivil/$', views.CivilLines, name='CivilLines'),

]