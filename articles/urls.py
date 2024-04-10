from unicodedata import name
from . import views
from django.urls import path, re_path

app_name= 'patients'

urlpatterns = [
    path('', views.article_list, name='articles'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.article_detail, name= "detail"),

]
