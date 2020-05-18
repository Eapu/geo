from django.contrib.gis.db import models
from django.core.validators import URLValidator
from django.db.models import Manager as GeoManager
from django.core.files import File
import urllib.request
import os
from django.utils import timezone

class Toledo(models.Model):

	pntnum = models.IntegerField()
	panoid = models.CharField(max_length=80)
	panodate = models.CharField(max_length=80)
	greenview = models.FloatField(max_length=6)
	url0 = models.CharField(max_length=200,blank=True, null=True)
	url60 = models.CharField(max_length=200,blank=True, null=True)
	url120 = models.CharField(max_length=200,blank=True, null=True)
	url180 = models.CharField(max_length=200,blank=True, null=True)
	url240 = models.CharField(max_length=200,blank=True, null=True)
	url300 = models.CharField(max_length=200,blank=True, null=True)
	geom = models.MultiPointField(srid=4326,blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Toledo'
	def save(self, *args, **kwargs):
		self.greenview = round(self.greenview, 2)
		super(Toledo, self).save(*args, **kwargs)

