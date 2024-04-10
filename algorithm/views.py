from audioop import reverse
#from crypt import methods
from operator import methodcaller
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from articles.decorator import allowed_users
from articles.models import User, Patient
from django.contrib.auth.decorators import login_required
from accounts import forms
from accounts.models import Patient_final
from articles.models import Patient_duration, Patient_test

def fire_ann(request):
    return HttpResponse("output")

@login_required(login_url="/accounts/login_admin/")
@allowed_users(allowed_groups=['Admin'])
def patient_testdetail(request, slug):
    #return HttpResponse(slug)
    patients = Patient_test.objects.get(NIC=slug)
    return render(request, 'patient_testdetail.html', {'Patient': patients})


