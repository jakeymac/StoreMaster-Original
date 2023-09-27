from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

from django.contrib.auth.models import User
from django import forms
from .models import *

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
    stores = Store.objects.all()
    context = {"stores":stores}
    if request.method == "POST":
        new_form = RegistrationForm(request.POST)
        if new_form.is_valid():
            username = new_form.cleaned_data["username"]
            password = new_form.cleaned_data["password"]
            email = new_form.cleaned_data["email"]

            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("This username is already in use")
            elif  User.objects.filter(email_address=email).exists():
                raise forms.ValidationError("This email is already in use")
            
            else:
                user = User(username=username, password=password, email=email)
                user.save()
        else:
            return HttpResponse("INVALID FORM")
    
        
    else:
        return render(request,"register_user.html",context)
    

    