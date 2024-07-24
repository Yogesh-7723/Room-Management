from django.shortcuts import render,redirect
from app1.models import *
from .models import Product
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth import  logout, authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def entry(request): 
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
    return  render(request,'first.html')

def log_out(request,qk):
    user = User.objects.get(id=qk)
    if user is not None:
        logout(request)
    return redirect('/sign_in/')


def data(request):
    if request.method == 'POST':
        user = request.POST['user']
        item = request.POST['item']
        price = request.POST['price']
        if user !='' and item != '' and price!='':
            print("Enter Every Values")
        Product.objects.create(user=user,item=item,price=price)
        messages.success(request,"Item Successfully Add !")
        return redirect('/add_product/')
    
    u_data = User.objects.all()
    return render(request,'data.html',{'u_data':u_data})

def menu(request):
    return render(request,"menu.html")

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
            return redirect('/signup/')
    else:
        return render(request,'signup.html')

def all_product(request):
    data = Product.objects.all()
    total = Product.objects.aggregate(total_price=Sum('price'))
    return render(request,'table.html',{'data':data,'total':total})
