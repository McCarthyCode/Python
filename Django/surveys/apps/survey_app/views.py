from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html', {})

def result(request):
    # initialize session variables to empty values
    values = {}
    for i in ['name', 'location', 'language', 'comment']:
        if i in request.session:
            values[i] = request.session[i]
    
    values['count'] = request.session['count']
    return render(request, 'result.html', values)

def submit(request):
    # start or increment the counter
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    #  store POST values in session to use in render route
    for i in ['name', 'location', 'language', 'comment']:
        request.session[i] = request.POST[i]
    
    return redirect('/result')
