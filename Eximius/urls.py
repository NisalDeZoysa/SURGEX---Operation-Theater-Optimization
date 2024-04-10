
from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls, name='Administration'),
    path('accounts/', include('accounts.urls')),
    path('', views.homepage, name='Home'),
    path('about/', views.about, name='About page'),
    path('patients/', include('articles.urls')),
    path('algorithms/', include('algorithm.urls')),
    path('genetic/', include('genetic.urls')),
]
