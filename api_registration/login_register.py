from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('login_db.db')
conn.cursor()


@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/register')
def new():
    return render_template('register_page.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        try:
            user_name = request.form['user_name']
            email = request.form['email']
            contact = request.form['ph_no']
            password = request.form['password']

            with sql.connect('login_db.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user_details(user_name, email, phone_no, password) VALUES (?, ?, ?, ?)",
                            (user_name, email, contact, password))
                msg = "Added details into database"
        except:
            con.rollback()
            msg = "Error..! couldn't insert the details into database"

        finally:
            return render_template("result.html", msg=msg)
        con.close()


@app.route('/login')
def login():
    return render_template('login_page.html')


@app.route('/check', methods=['POST', 'GET'])
def check():
    user_name = request.form['user_name']
    password = request.form['password']

    with sql.connect('login_db.db') as con:
        cur = con.cursor()
        c = cur.execute(f"SELECT * FROM user_details WHERE user_name='{user_name}' AND password='{password}';")
        if not c.fetchone():
            return render_template('register_page.html')

        else:
            return render_template('after_login.html')
    con.close()


app.run(debug=True)
