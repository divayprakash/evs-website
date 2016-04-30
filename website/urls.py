from django.conf.urls import url
from . import views

app_name='website'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^detail/$',views.pollutionInDelhi, name='pollutionInDelhi'),
    url(r'^IIITD/$', views.IIITD, name='IIITD'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^issue/$', views.issue, name='issue'),
    url(r'^detail/data/$', views.AnandVihar, name='AnandVihar'),

]