from datetime import date
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required
from .decorator import allowed_users
from accounts.models import Patient_final


@login_required(login_url="/accounts/login_doctor/")
@allowed_users(allowed_groups=['Doctor','Admin'])
def article_list(request):
    patients = Patient_final.objects.all()
    return render(request,'articles/article_list.html', {'Patients': patients})

@login_required(login_url="/accounts/login_doctor/")
@allowed_users(allowed_groups=['Doctor','Admin'])
def article_detail(request, slug):
    #return HttpResponse(slug)
    patients = Patient_final.objects.get(NIC=slug)
    return render(request, 'articles/patient_detail.html', {'Patient': patients})


# Create your views here.
