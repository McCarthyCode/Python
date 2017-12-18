from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'alohomora'
mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
    query =  'SELECT'
    query += '   name,'
    query += '   age,'
    query += '   DATE_FORMAT(date_created, "%M %D") AS friend_since,'
    query += '   DATE_FORMAT(date_created, "%Y") AS year '
    query += 'FROM friends;'
    result = mysql.query_db(query)

    return render_template('index.html', rows=result)

@app.route('/submit', methods=['POST'])
def submit():
    query = 'INSERT INTO friends (name, age) '
    query += 'VALUES (:name, :age);'
    data = {'name': request.form['name'], 'age': request.form['age']}

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
