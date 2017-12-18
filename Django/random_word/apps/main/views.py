from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    values = {
        'count': request.session['count'],
        'word': get_random_string(length=14)
    }

    return render(request, 'index.html', values)

def generate(request):
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    return redirect('/')
