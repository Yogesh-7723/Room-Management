from django.shortcuts import render,redirect
from app1.models import *
from .models import Product
from django.db.models import Sum
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import  logout, authenticate, login
from django.http import HttpResponse
from app1.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets

# Create your views here.
def index(request):
    if request.method=='POST':
        fm = ProductForm(request.data)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    data = Profile.objects.order_by("?")
    fm = ProductForm
    return render(request,'index.html',{'data':data,'fm':fm})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request,"Password Not Match ")
            return redirect('/signup/')
        
        elif User.objects.filter(username=username).exists():
            print("user already exists")
            return redirect('/signup/')
        else:
            pwd = make_password(password1)
            User.objects.create(username=username,email=email,password=pwd)
            print("successfull create account")
            messages.success(request,"Congrates Membership Successfull")
            return redirect('/sign_in/')
    else:
        return render(request,'accounts/signup.html')

def signin(request): 
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST.get('password')
        print(name,pwd)
        user = authenticate(username=name,password=pwd)
        print(user)
        if user is not None:
            login(request,user)
            print("login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid username and password")
            return redirect('/sign_in/')
    return  render(request,'accounts/signin.html')


def log_out(request,qk):
    user = User.objects.get(id=qk)
    if user is not None:
        logout(request)
    return redirect('/sign_in/')

def profile(request):
    if request.method=='POST':
        edu = request.POST['edu']
        contact = request.POST['contact']
        user = request.POST.get('username')
        gender = request.POST['gender']
        dept = request.POST['dept']
        address = request.POST['address']
        image = request.FILES.get('image')
        print(edu,contact,user,gender,dept,address,image)
    else:
        user = request.user
        data = Profile.objects.get(name=user)
    product = Product.objects.filter(user=user)
    total = Product.objects.filter(user=user).aggregate(total_amount=Sum('price'))
    current = Product.objects.filter(date=datetime.today(),user=user).aggregate(current_month = Sum('price'))
    print(total,current)
    return render(request,"accounts/profile.html",{'data':data,'product':product,'current':current,'total':total})
    
    


def data(request):
    if request.method == 'POST':
        user = request.user
        item = request.POST['item']
        price = request.POST['price']
        if user !='' and item != '' and price!='':
            print("Enter Every Values")
        if user.is_authenticated:
            Product.objects.create(user=user,item=item,price=price)
            messages.success(request,"Item Successfully Add !")
            return redirect('/add_product/')
    
    u_data = User.objects.all()
    return render(request,'data.html',{'u_data':u_data})

def menu(request):
    return render(request,"menu.html")

def all_product(request):
    data = Product.objects.all()
    total = Product.objects.aggregate(total_amount=Sum('price'))
    # rohit = Product.objects.filter(name='Rohit').aggregate(rohit_amount = Sum('price'))
    # lucky = Product.objects.filter(name='Lucky').aggregate(lucky_amount = Sum('price'))
    current = Product.objects.filter(date=datetime.today()).aggregate(current_month = Sum('price'))
    return render(request,'table.html',{'data':data,'total':total,'current':current})

def delete_data(request,qk):
    Product.objects.get(id=qk).delete()
    messages.success(request,"Product Successfully Delete.")
    return redirect('/profile/')

