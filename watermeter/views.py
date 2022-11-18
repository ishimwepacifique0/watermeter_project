from select import select
from django.shortcuts import render,redirect
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            # login(request,user)
            return render(request,'dashboard.html')

        else:
            messages.error(request,"you have not loggd in")
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('logout')

def dashboard(request):
    return render(request,'index.html')

def new_employer(request):
    if request.method == "POST":
        post = Employer()
        post.firstname = request.POST['firstname']
        post.lastname = request.POST['lastname']
        post.National_id = request.POST['national_id']
        post.email = request.POST['email']
        post.gender = request.POST['gender']
        post.job_title = request.POST['jobtitle']
        post.save()
    return render(request,'new_employer.html')


def manage_employer(request):
    selectdata = Employer.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_employes.html',context)

def delete_employer(request,id):
    selectdata = Employer.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_employer')


def new_customer(request):
    selectdata = Customer.objects.all()
    if request.method == "POST":
        post = Customer()
        post.watermeterid = request.POST['wid']
        post.address = request.POST['address']
        post.names = request.POST['fullname']
        post.email = request.POST['email']
        post.gender = request.POST['gender']
        post.phonenumber = request.POST['phonenumber']
        post.National_id  = request.POST['national_id']
        post.save()
    return render(request,'new_customer.html',{"data":selectdata})

################ detial of the customer ###################

def manage_customer(request):
    selectdata = Customer.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_customer.html',context)

def delete_customer(request,id):
    selectdata = Customer.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_customer')


def add_watermeter(request):
    if request.method == "POST":
        post = watermeter()
        post.address = request.POST['address']
        post.ownername = request.POST['ownername']
        post.save()
    return render(request,'add_watermeter.html')

def manage_watermeter(request):
    selectdata = watermeter.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_watermeter.html',context)

def delete_watermeter(request,id):
    selectdata = watermeter.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_watermeter')


def new_bill(request):
    selectdata = Bill.objects.all()
    if request.method == "POST":
        post = Bill()
        post.w_id = request.POST['watermeterid']
        post.data = request.POST['data']
        post.bill_piad = request.POST['bill_piad']
        post.bill_owner = request.POST['bill_owner']
        post.save()
    return render(request,'new_bill.html',{"data":selectdata})

def manage_bill(request):
    selectdata = Bill.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_bill.html',context)

def delete_bill(request,id):
    selectdata = Bill.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_bill')


######## frontend ##########

def home(request):
    return render(request,'fontend/index.html')