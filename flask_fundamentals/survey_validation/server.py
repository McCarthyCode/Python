from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'alohomora'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    errorsExist = False

    if len(request.form['name']) < 1:
        flash("Name cannot be blank.")
        errorsExist = True
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank.")
        errorsExist = True
    if len(request.form['comment']) > 120:
        flash("Comment cannot be more than 120 characters.")
        errorsExist = True
    
    if errorsExist:
        return redirect('/')

    return render_template(
        'result.html',
        name = request.form['name'],
        location = request.form['location'],
        language = request.form['language'],
        comment = request.form['comment']
        )

app.run(debug=True)
