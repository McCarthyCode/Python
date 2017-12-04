from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
@app.route('/ninjas/')
def ninja():
    return render_template('ninja.html', title='Ninjas')

@app.route('/ninjas/<color>')
def ninjas(color):
    if color == 'blue':
        return render_template('ninja.html', title='Leonardo')
    elif color == 'orange':
        return render_template('ninja.html', title='Michelangelo')
    elif color == 'red':
        return render_template('ninja.html', title='Raphael')
    elif color == 'purple':
        return render_template('ninja.html', title='Donatello')
    else:
        return render_template('ninja.html', title='Not a ninja')

app.run(debug=True)
