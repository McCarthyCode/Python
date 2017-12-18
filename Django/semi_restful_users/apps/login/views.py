from django.shortcuts import render, HttpResponse, redirect
from .models import User, UserManager
from django.contrib import messages

def home(request):
    return render(request, 'login/index.html')

def register(request):
    um = UserManager()
    valid, response = um.validate(request.POST, 'register')
    if not valid:
        for message in response:
            messages.error(request, message)
        return redirect('home')

    return redirect('success')

def login(request):
    um = UserManager()
    valid, response = um.validate(request.POST, 'login')
    if not valid:
        for message in response:
            messages.error(request, message)
        return redirect('home')
    return redirect('success')

def success(request):
    return render(request, 'login/success.html')
