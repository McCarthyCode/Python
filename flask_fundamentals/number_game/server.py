from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'alohomora'

@app.route('/')
def index():
    num = random.randrange(1, 101)
    if 'number' not in session:
        session['number'] = num
        session['answered'] = False

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['answered'] = True
    session['input'] = int(request.form['number'])
    return redirect('/')

@app.route('/reset')
def reset():
    del session['number']
    return redirect('/')

app.run(debug=True)
