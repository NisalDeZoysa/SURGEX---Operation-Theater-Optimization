from audioop import reverse
#from crypt import methods
from operator import methodcaller
from unicodedata import name
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from articles.decorator import allowed_users
from articles.models import User, Patient
from django.contrib.auth.decorators import login_required 
from . import forms
from .models import Patient_final
from articles.models import Patient_duration, Patient_test
from .nurel import ann







def signup_view_p(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, 'accounts/verification.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_p.html', {'form': form})

def signup_view_d(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, 'accounts/verification.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_d.html', {'form': form})

@login_required(login_url="/accounts/login_patient/")
@allowed_users(allowed_groups=['Patient'])
def patient_home(request):
    return render(request, 'accounts/personalaccount.html')

@login_required(login_url="/accounts/login_doctor/")
@allowed_users(allowed_groups=['Doctor'])
def doctor_home(request):
    return render(request, 'accounts/doctoraccount.html')


def login_view_p(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('accounts:home_p')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login_patient.html', {'form': form})

def login_view_d(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('accounts:home_d')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login_doctor.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect( 'homepage.html')
#this
@login_required(login_url="/accounts/login_patient/")
@allowed_users(allowed_groups=['Patient'])
def myaccount_p(request,pk_test):
    user = User.objects.get(id=pk_test)
    context = {'user':user}
    return render(request, 'accounts/myaccount_p.html',context)

@login_required(login_url="/accounts/login_doctor/")
@allowed_users(allowed_groups=['Doctor'])
def myaccount_d(request,pk_test):
    user = User.objects.get(id=pk_test)
    context = {'user':user}
    return render(request, 'accounts/myaccount_d.html',context)

#@login_required(login_url="/accounts/login_doctor/")
#@allowed_users(allowed_groups=['Doctor'])
#def surgery_create(request):
#    if request.method == 'POST':
#        form=forms.patient_form(request.POST)
#        if form.is_valid:
#            form.save()
#            return redirect('algorithms:ann')
#    else:
#        form = forms.patient_form()
#    return render(request,'articles/article_create.html', {'form' : form})
#meka wenuwata pahalin demme function eka

@login_required(login_url="/accounts/login_doctor/")
@allowed_users(allowed_groups=['Doctor'])
def surgery_create(request):
    form=forms.patient_form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        print(data)
        age = data['age']
        #NIC= data['NIC']
        gender = data['gender']
        bmi = data['BMI']
        situation = data['situation']
        seriousness = data['seriousness']
        sur_type = data['surgery_type']
        print("nisal")
        predicted = ann(age,gender,bmi,situation,sur_type,seriousness)
        
        print(predicted)
        

        print(age)
        #print(NIC)
        #    form.save()
        #    return redirect('algorithms:ann')
    else:
        form = forms.patient_form()
    return render(request,'articles/article_create.html', {'form' : form})


def administration(request):
    return render(request, 'accounts/administration.html')


def login_view_a(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('accounts:administration_account')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login_admin.html', {'form': form})

@login_required(login_url="/accounts/login_admin/")
@allowed_users(allowed_groups=['Admin'])
def administration_account(request):
    return render(request, 'accounts/administrationaccount.html')


@allowed_users(allowed_groups=['Doctor','Admin'])
def patient_testlist(request):
    patients = Patient_test.objects.all()
    return render(request,'accounts/Patient_testlist.html', {'Patients': patients})
    

