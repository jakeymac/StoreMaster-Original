from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "login_registration_home.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("Successfully Logged in")
        else:
            return render(request,"login_user.html",{"error_message":"Invalid"})
    else:

        return render(request,"login_user.html",{})

def register_user(request):
    return HttpResponse("Register User Page")