from django.db import models


class Area(models.Model):
    area_name=models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.area_name) or u''


class Pollutants(models.Model):
    Name=models.ForeignKey(Area,on_delete=models.CASCADE)
    param=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    concen=models.CharField(max_length=100)
    standard=models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.param) or u''

# Create your models here.