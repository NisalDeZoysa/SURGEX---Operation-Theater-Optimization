from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path, include,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from unicodedata import name


app_name= 'algorithms'

urlpatterns = [
    path('ann/', views.fire_ann, name='ann'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.patient_testdetail, name= "testdetail"),

]
