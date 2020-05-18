# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Toledo
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

 
class ToledoAdmin(LeafletGeoAdmin):
	#pass
	list_display =('pntnum','panoid','panodate', 'greenview')

admin.site.register(Toledo, ToledoAdmin)