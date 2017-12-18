from django.shortcuts import render, HttpResponse, redirect
import time
import random

def index(request):
    if 'gold' not in request.session or 'history' not in request.session:
        request.session['gold'] = 0
        request.session['history'] = []
        return redirect('/')

    return render(request, 'index.html', {})


def process_money(request):
    string = time.ctime(time.time())

    if request.POST['building'] == 'farm':
        gold = random.randrange(10, 21)
        string += " Earned "
        string += str(gold)
        string += " gold from the farm!"
    elif request.POST['building'] == 'cave':
        gold = random.randrange(5, 11)
        string += " Earned "
        string += str(gold)
        string += " gold from the cave!"
    elif request.POST['building'] == 'house':
        gold = random.randrange(2, 6)
        string += " Earned "
        string += str(gold)
        string += " gold from the house!"
    elif request.POST['building'] == 'casino':
        gold = random.randrange(-50, 51)
        if gold < 0:
            string += " Entered a casino and lost "
            string += str(abs(gold))
            string += " gold... Ouch..."
            # Let's not deduct into negative values
            if abs(gold) > request.session['gold']:
                request.session['gold'] = 0
                gold = 0
        elif gold == 0:
            string += " Entered a casino and broke even. That's fine, I guess."
        else:
            string += " Entered a casino and won "
            string += str(gold)
            string += " gold!"

    request.session['gold'] += gold
    request.session['history'].append(string)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
