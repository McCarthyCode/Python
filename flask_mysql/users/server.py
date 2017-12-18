from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'alohomora'
mysql = MySQLConnector(app, 'users')

@app.route('/users')
def index():
    query =  'SELECT'
    query += '   id,'
    query += '   first_name,'
    query += '   last_name,'
    query += '   email,'
    query += '   DATE_FORMAT(date_created, "%M %D, %Y") AS date '
    query += 'FROM users;'
    result = mysql.query_db(query)

    return render_template('index.html', rows=result)

@app.route('/users/new')
def new():
    # define session variables with empty values on initial route
    fields = ['first_name', 'last_name', 'email']
    for i in fields:
        if i not in session:
            session[i] = ''

    return render_template('new.html')


@app.route('/users/<id>/edit')
def edit(id):
    # define session variables with empty values on initial route
    fields = ['first_name', 'last_name', 'email']
    for i in fields:
        if i not in session:
            session[i] = ''

    return render_template('edit.html', id=id)

@app.route('/users/<id>')
def show(id):
    query =  'SELECT'
    query += '   id,'
    query += '   first_name,'
    query += '   last_name,'
    query += '   email,'
    query += '   DATE_FORMAT(date_created, "%M %D, %Y") AS date '
    query += 'FROM users '
    query += 'WHERE id = :id;'
    data = {'id': id}
    result = mysql.query_db(query, data)

    return render_template('show.html', rows=result)

@app.route('/users/create', methods=['POST'])
def create():
    # store values in session variables
    for i in ['first_name', 'last_name', 'email']:
        session[i] = request.form[i]

    # obtain form values
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    # define regular expressions and error flag
    # note: the following email regex is used in <input type='email'> from W3C
    # (except here the apostrophe character is replaced with its unicode value)
    email_regex = re.compile(
        r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    name_regex = re.compile(r'^[a-zA-Z]+$')
    errors_exist = False

    # make sure there are no blank fields
    print 'line 53'
    for i in request.form:
        if len(request.form[i]) == 0:
            flash('Error: All fields are required.', 'error')
            errors_exist = True
            break

    # first and last name may only contain letters
    if len(first_name) < 2 or len(last_name) < 2:
        flash('Error: First and last name must contain at least two characters.', 'error')
        errors_exist = True
    elif not name_regex.match(first_name) or not name_regex.match(last_name):
        flash('Error: First and last name may not contain numbers or special characters.', 'error')
        errors_exist = True

    # email format should be valid
    if len(email) > 0 and not email_regex.match(email):
        flash('Error: Invalid email format.', 'error')
        errors_exist = True

    # return to form if errors exist
    if errors_exist:
        return redirect('/users/new')

    # otherwise, add values to database
    query =  'INSERT INTO users (first_name, last_name, email) '
    query += 'VALUES (:first_name, :last_name, :email);'
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email}
    mysql.query_db(query, data)

    session.clear()
    return redirect('/users')

@app.route('/users/<id>/destroy')
def destroy(id):
    # delete row in database
    query =  'DELETE FROM users WHERE id = :id;'
    data = {'id': id}
    mysql.query_db(query, data)

    return redirect('/users')

@app.route('/users/<id>', methods=['POST'])
def update(id):
    # store values in session variables
    for i in ['first_name', 'last_name', 'email']:
        session[i] = request.form[i]

    # obtain form values
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    # define regular expressions and error flag
    # note: the following email regex is used in <input type='email'> from W3C
    # (except here the apostrophe character is replaced with its unicode value)
    email_regex = re.compile(
        r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    name_regex = re.compile(r'^[a-zA-Z]+$')
    errors_exist = False

    # make sure there are no blank fields
    print 'line 53'
    for i in request.form:
        if len(request.form[i]) == 0:
            flash('Error: All fields are required.', 'error')
            errors_exist = True
            break

    # first and last name may only contain letters
    if len(first_name) < 2 or len(last_name) < 2:
        flash('Error: First and last name must contain at least two characters.', 'error')
        errors_exist = True
    elif not name_regex.match(first_name) or not name_regex.match(last_name):
        flash('Error: First and last name may not contain numbers or special characters.', 'error')
        errors_exist = True

    # email format should be valid
    if len(email) > 0 and not email_regex.match(email):
        flash('Error: Invalid email format.', 'error')
        errors_exist = True

    # return to form if errors exist
    if errors_exist:
        return redirect('/users/' + id + '/edit')

    # otherwise, update row in database
    query =  'UPDATE users '
    query += 'SET'
    query += '   first_name=:first_name,'
    query += '   last_name=:last_name,'
    query += '   email=:email,'
    query += '   date_updated=NOW() '
    query += 'WHERE id = :id;'
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'id': id}
    mysql.query_db(query, data)

    session.clear()
    return redirect('/users/' + id)

app.run(debug=True)
