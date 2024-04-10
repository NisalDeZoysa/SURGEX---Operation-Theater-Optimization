from unicodedata import name
from . import views
from django.urls import path, re_path


app_name ='accounts'

urlpatterns = [
    path('signup_p/',views.signup_view_p, name="signup_p"),
    path('patient_testlist/',views.patient_testlist, name="testlist"),
    path('signup_d/',views.signup_view_d, name="signup_d"),
    path('userhome_p/',views.patient_home, name="home_p"),
    path('userhome_d/',views.doctor_home, name="home_d"),
    path('login_patient/', views.login_view_p, name="login_patient"),
    path('login_doctor/', views.login_view_d, name="login_doctor"),
    path('login_admin/', views.login_view_a, name="login_admin"),
    path('logout/', views.logout_view, name="logout"),
    path('myaccount_p/<str:pk_test>/', views.myaccount_p, name="myaccount_p"),
    path('myaccount_d/<str:pk_test>/', views.myaccount_d, name="myaccount_d"),
    path('newsurgery/', views.surgery_create, name='new'),
    path('administration/', views.administration, name= 'administration'),
    path('administration_account/', views.administration_account, name= 'administration_account'),
    
]