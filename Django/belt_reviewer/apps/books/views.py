from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from ..login.models import User, UserManager

def index(request):
    if 'id' not in request.session:
        redirect(reverse('login:index'))
    content = {
        'name': User.objects.get(id=request.session['id']).first_name
    }
    return render(request, 'books/index.html', content)

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

def add(request):
    return render(request, 'books/add.html')
