from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    time = gmtime()
    context = {
        'date': strftime("%b %d, %Y", time),
        'time': strftime("%-I:%M %p GMT", time),
        }
    return render(request, 'index.html', context)

def time_display(request):
    return redirect('/')
