from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, UserManager

def index(request):
    return render(request, 'login/index.html')

def register(request):
    um = UserManager()
    valid, response = um.validate(request.POST, 'register')
    if not valid:
        for message in response:
            messages.error(request, message)
        return redirect(reverse('login:index'))
    else:
        request.session['id'] = response.id

    return redirect(reverse('books:index'))

def login(request):
    um = UserManager()
    valid, response = um.validate(request.POST, 'login')
    if not valid:
        for message in response:
            messages.error(request, message)
        return redirect(reverse('login:index'))
    else:
        request.session['id'] = response.id

    return redirect(reverse('books:index'))
