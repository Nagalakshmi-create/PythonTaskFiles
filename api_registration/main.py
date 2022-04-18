from flask import Flask, render_template, request, jsonify

import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('database.db')
conn.cursor()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enter')
def new():
    return render_template('new.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
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
    return render_template('login.html')


@app.route('/check',methods=['POST', 'GET'])
def check():
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


app.run()