from django.conf.urls import include,url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'GEO'

urlpatterns = [

	url(r'^$', views.home, name = 'home'),
	url(r'^toledo_datasets/$', views.toledo_datasets, name = 'toledo_datasets'),

	]
