from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, os, hashlib, binascii

app = Flask(__name__)
app.secret_key = 'alohomora'
mysql = MySQLConnector(app, 'wall')

@app.route('/')
def index():
    # define session variables with empty values on initial route
    fields = ['first_name', 'last_name', 'email', 'email_login']
    for i in fields:
        if i not in session:
            session[i] = ''
    session['verified'] = False

    return render_template('index.html')

@app.route('/wall')
def wall():
    # verify user is logged in
    if 'id' not in session:
        return redirect('/')

    # retrieve first name of user to display in template
    query =  'SELECT '
    query += '    first_name '
    query += 'FROM users '
    query += 'WHERE id = :id;'
    data = {'id': session['id']}
    result = mysql.query_db(query, data)
    name = result[0]['first_name']

    # retrieve messages from database
    query = 'SELECT'
    query += '    users.id AS user_id,'
    query += '    messages.id AS message_id,'
    query += '    first_name,'
    query += '    last_name,'
    query += '    message,'
    query += '    DATE_FORMAT(messages.date_created, "%M %D, %Y") AS date_posted '
    query += 'FROM messages '
    query += 'JOIN users ON users.id = messages.user_id '
    query += 'ORDER BY messages.date_created DESC'
    messages = mysql.query_db(query)

    # retrieve comments from database
    query =  'SELECT'
    query += '    users.first_name,'
    query += '    users.last_name,'
    query += '    message_id,'
    query += '    comment,'
    query += '    DATE_FORMAT(comments.date_created, "%M %D, %Y") AS date_posted '
    query += 'FROM comments '
    query += 'JOIN users ON users.id = comments.user_id '
    query += 'ORDER BY date_posted ASC;'
    comments = mysql.query_db(query)

    return render_template('wall.html', name=name, messages=messages, comments=comments)

@app.route('/message', methods=['POST'])
def message():
    # add message to database
    query =  'INSERT INTO messages '
    query += '('
    query += '    user_id, '
    query += '    message, '
    query += '    date_created, '
    query += '    date_updated'
    query += ') '
    query += 'VALUES '
    query += '('
    query += '    :user_id, '
    query += '    :message,'
    query += '    NOW(),'
    query += '    NOW()'
    query += ');'
    data = {
        'user_id': session['id'],
        'message': request.form['message']
        }
    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    # add comment to database
    query =  'INSERT INTO comments '
    query += '('
    query += '    user_id, '
    query += '    message_id, '
    query += '    comment, '
    query += '    date_created, '
    query += '    date_updated'
    query += ') '
    query += 'VALUES '
    query += '('
    query += '    :user_id, '
    query += '    :message_id,'
    query += '    :comment, '
    query += '    NOW(),'
    query += '    NOW()'
    query += ');'
    data = {
        'user_id': session['id'],
        'message_id': request.form['message_id'],
        'comment': request.form['comment']
    }
    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/register', methods=['POST'])
def register():
    # store values in session variables
    for i in ['first_name', 'last_name', 'email']:
        session[i] = request.form[i]

    # obtain form values
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # define regular expressions and error flag
    # note: the following email regex is used in <input type='email'> from W3C
    # (except here the apostrophe character is replaced with its unicode value)
    email_regex = re.compile(
        r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    name_regex = re.compile(r'^[a-zA-Z]+$')
    password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d).{8,}$')
    errors_exist = False

    # make sure there are no blank fields
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

    # password must be of at least medium strength
    if not password_regex.match(password):
        message = 'Error: Password must be at least 8 characters in length '
        message += 'containing at least 1 uppercase letter, at least 1 number, and no spaces.'
        flash(message, 'error')
        errors_exist = True

    # passwords should match
    if password != confirm_password:
        flash('Error: Passwords do not match.', 'error')
        errors_exist = True
    
    # check database for duplicate entries
    query = 'SELECT * FROM users '
    query += 'WHERE email = :email'
    data = {'email': email}
    result = mysql.query_db(query, data)
    if result != []:
        flash('Error: An account is already registered with that email.', 'error')
        errors_exist = True
    
    # create database entry if all criteria are met
    if not errors_exist:
        # hash password
        salt = binascii.b2a_hex(os.urandom(16))
        hashed_pw = hashlib.sha256(salt + password).hexdigest()

        # store data in database
        query =  'INSERT INTO users '
        query += '('
        query += '    first_name,'
        query += '    last_name,'
        query += '    email,'
        query += '    password,'
        query += '    salt'
        query += ') '
        query += 'VALUES '
        query += '('
        query += '    :first_name,'
        query += '    :last_name,'
        query += '    :email,'
        query += '    :password,'
        query += '    :salt'
        query += ');'
        data = {
            'first_name': first_name, 
            'last_name': last_name,
            'email': email,
            'password': hashed_pw,
            'salt': salt}
        mysql.query_db(query, data)

        session.clear()
        flash('You have successfully registered.')
    
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    # prevent user from deleting posts other than their own
    message_id = int(request.form['message_id'])
    user_id = int(request.form['user_id'])
    if user_id != session['id']:
        session.clear()
        flash('Error: user in session does not match user of message', 'error')
        return redirect('/')

    # delete message from database
    query =  'DELETE FROM messages '
    query += 'WHERE id = :message_id;'
    data = {'message_id': message_id}
    print query, data
    mysql.query_db(query, data)
    
    # delete corresponding comments from database
    query =  'DELETE FROM comments '
    query += 'WHERE message_id = :message_id;'
    data = {'message_id': request.form['message_id']}
    print query, data
    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    # define form input as local variables
    email = request.form['email']
    password = request.form['password']
    session['email_login'] = email

    # email format should be valid
    email_regex = re.compile(
        r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    if len(email) > 0 and not email_regex.match(email):
        flash('Error: Invalid email format.', 'error')
        return redirect('/')
    
    # retrieve hashed password and salt from database that corresponds to given email
    query =  'SELECT '
    query += '    id,'
    query += '    password,'
    query += '    salt '
    query += 'FROM users '
    query += 'WHERE email = :email;'
    data = {'email': email}
    result = mysql.query_db(query, data)

    # check if email is in database
    if result == []:
        flash('Error: No account is registered with that email.', 'error')
        return redirect('/')
    
    # authenticate password
    hashed_pw = result[0]['password']
    salt = result[0]['salt']
    if hashlib.sha256(salt + password).hexdigest() == hashed_pw:
        # clear session, but store user id
        session.clear()
        session['id'] = result[0]['id']
        
        return redirect('/wall')
    else:
        flash('Password is incorrect.', 'error')

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
