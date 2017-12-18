from flask import Flask, render_template, request, redirect, session, flash
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'alohomora'

@app.route('/')
def index():
    # define session variables with empty values on initial route
    fields = ['email', 'first_name', 'last_name', 'birthday']
    for i in fields:
        if i not in session:
            session[i] = ''
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # store values in session variables
    for i in ['email', 'first_name', 'last_name', 'birthday']:
        session[i] = request.form[i]

    # define regular expressions and error flag
    # note: the following email regex is used in <input type='email'> from W3C
    # (except here the apostrophe character is replaced with its unicode value)
    email_regex = re.compile(
        r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    name_regex = re.compile(r'^[a-zA-Z]+$')
    past_date_regex = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d).{8,}$')
    errors_exist = False
    
    # make sure there are no blank fields
    for i in request.form:
        if len(request.form[i]) == 0:
            flash('Error: All fields are required.', 'error')
            errors_exist = True
            break

    # email format should be valid
    if len(request.form['email']) > 0 and not email_regex.match(request.form['email']):
        flash('Error: Invalid email format.', 'error')
        errors_exist = True
    
    # first and last name may only contain letters
    if (len(request.form['first_name']) == 0 or not name_regex.match(request.form['first_name'])) and (len(request.form['last_name']) or not name_regex.match(request.form['last_name'])) == 0:
        flash('Error: First and last name may not contain numbers or special characters.', 'error')
        errors_exist = True
    
    # birthday should be a valid date from the past
    if len(request.form['birthday']) == 0:
        pass
    elif not past_date_regex.match(request.form['birthday']):
        flash('Error: Birthday must be in format MM/DD/YYYY.', 'error')
        errors_exist = True
    else:
        birthday = datetime.strptime(request.form['birthday'], '%m/%d/%Y')
        if birthday > datetime.now():
            flash('Error: Birthday cannot be in the future. If you are a time traveler, ' +
                    'please contact support and we will remedy the issue.', 'error')
            errors_exist = True
    
    # password must be of at least medium strength
    if not password_regex.match(request.form['password']):
        message = 'Error: Password must be at least 8 characters in length '
        message += 'containing at least 1 uppercase letter, at least 1 number, and no spaces.'
        flash(message, 'error')
        errors_exist = True

    # passwords should match
    if request.form['password'] != request.form['confirm_password']:
        flash('Error: Passwords do not match.', 'error')
        errors_exist = True

    # flash a happy green alert if all criteria are met
    if not errors_exist:
        session.clear()
        flash('Your information has been submitted successfully.')
    
    return redirect('/')

app.run(debug=True)
