from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_registration_page(request):
  
        return render(request, "Store/login_registration_home.html",{})

def store_home(request):
    return HttpResponse("This is a store home")

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmed_password = request.POST["password_confirmation"]
        #check password was confirmed
        if password == confirmed_password:
            pass
        else:
            pass
    return render(request, "Store/user_registration_page.html",{})

def register_customer(request):
     pass

def register_store(request):
    return HttpResponse("Register Store - Form")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            
            return HttpResponse("Success")
        else:
            messages.success(request, ("There was an Error logging in, try again..."))
            return redirect("/login")
    else:
        return render(request, "Store/login_page.html", {})
    
def login_success(request):
     pass



