from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'alohomora'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    
    return render_template('index.html')

@app.route('/plus_two')
def plus_two():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
