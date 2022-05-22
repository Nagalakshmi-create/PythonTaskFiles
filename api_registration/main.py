from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('database.db')
conn.cursor()


@app.route('/')
def home():
    ''' It displays links for login and registration pages '''
    return render_template('home.html')


@app.route('/enter')
def new():
    ''' It diaplays form for registration '''
    return render_template('new.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    ''' It adds user to the database if there is no error otherwise it shows error message '''
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            contact = request.form['contact']
            password = request.form['pwd']

            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute('''INSERT INTO details(name,email,contact,password) VALUES (?,?,?,?)''',(name,email,contact,password))
                msg = "Added"

        except:
            con.rollback()
            msg = "Error..!couldn't insert"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/login')
def login():
    ''' It displays login page to login '''
    return render_template('login.html')


@app.route('/check',methods=['POST', 'GET'])
def check():
    ''' It checks whether the user has an account or not. If the account is exists it displays
        Neosoft home page else it diaplays registration page to register '''
    name = request.form['name']
    password = request.form['pwd']

    with sql.connect('database.db') as con:
        cur = con.cursor()
        c = cur.execute(f"SELECT * from details WHERE name='{name}' AND password='{password}';")
        if not c.fetchone():
            return render_template('new.html')
        else:
            return render_template('after_login.html')
    con.close()


app.run(debug = True)
