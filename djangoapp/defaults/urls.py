from django.contrib import admin
#from django.conf.urls import url,include
from django.urls import path, include
from . import views

urlpatterns = [
	path('signup', views.signup),
	]
