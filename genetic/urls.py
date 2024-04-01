from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path, include,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from unicodedata import name


app_name= 'genetic'

urlpatterns = [

    path('ga/', views.fire_genetic, name= 'genetic_a')

]
