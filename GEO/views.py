from django.shortcuts import render
from .models import Toledo
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.gis import geos

def home(request):	
	return render(request, 'GEO/index.html')

def toledo_datasets(request):
	toledo_as_geojson = serialize('geojson', Toledo.objects.all())
	return HttpResponse(toledo_as_geojson,content_type='json')


