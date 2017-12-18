from django.shortcuts import render, HttpResponse, redirect
from .models import User, UserManager
from django.contrib import messages

def index(request):
    content = {
        'users': User.objects.all()
    }
    print content['users']
    return render(request, 'rest/index.html', content)

def new(request):
    return render(request, 'rest/new.html')

def edit(request, user_id):
    content = {
        'user_id': user_id,
        'first_name': User.objects.get(id=user_id).first_name,
        'last_name': User.objects.get(id=user_id).last_name,
        'email': User.objects.get(id=user_id).email,
        }
    return render(request, 'rest/edit.html', content)

def show(request, user_id):
    content = {
        'user_id': user_id,
        'first_name': User.objects.get(id=user_id).first_name,
        'last_name': User.objects.get(id=user_id).last_name,
        'email': User.objects.get(id=user_id).email,
        'created_at': User.objects.get(id=user_id).created_at,
    }
    return render(request, 'rest/show.html', content)

def create(request):
    um = UserManager()
    valid, response = um.validate(request.POST, 'create')
    if not valid:
        for message in response:
            messages.error(request, message)
        return redirect('new')

    return redirect('index')

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('index')


def update(request):
    um = UserManager()
    valid, response = um.validate(request.POST, 'update')
    if not valid:
        for message in response:
            messages.error(request, message)
        return redirect('edit', user_id=request.POST['user_id'])
    else:
        User.objects.get(id=request.POST['user_id'])
        return redirect('index')
