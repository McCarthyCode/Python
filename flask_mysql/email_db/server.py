from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'alohomora'
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    # flash('Email is not valid.', 'error')

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    email_regex = re.compile(
        r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    errors_exist = False

    if len(email) == 0:
        flash('Error: Email cannot be blank.', 'error')
        errors_exist = True
    elif not email_regex.match(email):
        flash('Error: Invalid email format.', 'error')
        errors_exist = True
    
    if errors_exist:
        return redirect('/')
    
    query =  'INSERT INTO emails(email)'
    query += 'VALUES(:email)'
    data = {'email': email}
    mysql.query_db(query, data)
    
    flash('The email address you entered (' + email + ') is a valid email address. Thank you!')
    return redirect('/success')

@app.route('/success')
def success():
    query =  'SELECT'
    query += '   email,'
    query += '   DATE_FORMAT(date_created, "%m/%d/%y %h:%i%p") AS date_added, '
    query += '   id '
    query += 'FROM emails '
    query += 'ORDER BY date_created DESC;'
    result = mysql.query_db(query)
    return render_template('success.html', rows=result)

@app.route('/delete', methods=['POST'])
def delete():
    query = 'DELETE FROM emails WHERE id = :id;'
    data = {'id': request.form['id']}
    mysql.query_db(query, data)

    flash('Email deleted successfully.')

    return redirect('/success')

app.run(debug=True)
