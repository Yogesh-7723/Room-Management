from django.shortcuts import render,redirect
from app1.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def entry(request):
    return  render(request,'first.html')

def index(request):
    return render(request,'index.html')

def data(request):
    return render(request,'data.html')

def menu(request):
    return render(request,"menu.html")

def signup(request):
    return render(request,'signup.html')

def ragistration(request):
    if request.method == 'POST':
        mem_name = request.POST['mem_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(mem_name=mem_name).exists():
            return HttpResponse('Usr Name Already Exists')
        
        elif User.objects.filter(email=email).exists():
            return HttpResponse('Email Already Exists')
        
        
        elif User.objects.filter(password=password).exists():
            return HttpResponse('Password Already Exists')    
        
        else:
            User.objects.create(mem_name=mem_name,email=email,
                        phone=phone,password=password)
            messages.success(request,'Ragistration Successfull')
            return redirect('/')
        

def product(request):
    if request.method == 'POST':
        name = request.POST['name']
        product = request.POST['product']
        amount = request.POST['amount']
        date = request.POST.get('date')
        if True:
            Purches.objects.create(name=name,product=product,amount=amount,date=date)
            return HttpResponse("Successfully")
        
        
def table(request):
    data = Purches.objects.all()
    return render(request,'table.html',{"data":data})



def delete(requered,pk):
    Purches.objects.get(id=pk).delete()
    return redirect("/table/")

