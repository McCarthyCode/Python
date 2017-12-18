from flask import Flask, render_template, request, redirect, session
import random
import time

app = Flask(__name__)
app.secret_key = 'alohomora'

@app.route('/')
def index():
    if 'gold' not in session or 'history' not in session:
        session['gold'] = 0
        session['history'] = []
        return redirect('/')

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    string = time.ctime(time.time())

    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        string += " Earned "
        string += str(gold)
        string += " gold from the farm!"
    elif request.form['building'] == 'cave':
        gold = random.randrange(5, 11)
        string += " Earned "
        string += str(gold)
        string += " gold from the cave!"
    elif request.form['building'] == 'house':
        gold = random.randrange(2, 6)
        string += " Earned "
        string += str(gold)
        string += " gold from the house!"
    elif request.form['building'] == 'casino':
        gold = random.randrange(-50, 51)
        if gold < 0:
            string += " Entered a casino and lost "
            string += str(abs(gold))
            string += " gold... Ouch..."
            if abs(gold) > session['gold']: # Let's not deduct into negative values
                session['gold'] = 0
                gold = 0
        elif gold == 0:
            string += " Entered a casino and broke even. That's fine, I guess."
        else:
            string += " Entered a casino and won "
            string += str(gold)
            string += " gold!"

    session['gold'] += gold
    session['history'].append(string)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
