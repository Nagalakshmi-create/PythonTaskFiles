from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)

conn = mysql.connector.connect(host="localhost", user="root", database="flaskapp")
# print("Successfully Connected Database")
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE user_details(user_name VARCHAR(100), email VARCHAR(200),
# phone_no VARCHAR(20), password VARCHAR(100))""")
# print("Successfully Created Table")


@app.route('/')
def home():
    """Displays home page which contains links for register and login pages."""
    return render_template("home_page.html")


@app.route('/register')
def register():
    """Displays register page which takes the user details and stores into the database."""
    return render_template("registration_page.html")


@app.route('/login')
def login():
    """Displays login page which takes username and password for authentication."""
    return render_template("login_page.html")


@app.route('/result')
def result():
    return render_template("success_page.html")


@app.route('/add_user', methods=['POST'])
def adding_user():
    """It stores user details into database when user submit the button
       and those values are accessed using name attribute value and successful message is displayed.
       If the details doesn't store into the database then message is displayed.
    """
    if request.method == 'POST':
        msg = ""
        try:
            user_name = request.form['user_name']
            email = request.form['email']
            contact = request.form['ph_no']
            password = request.form['password']

            cursor.execute("""INSERT INTO user_details(user_name, email, phone_no, password) 
                              VALUES (%s, %s, %s, %s)""", (user_name, email, contact, password))
            print("Successfully Inserted")
            msg = "Successfully added details into the database."
            conn.commit()
            conn.close()
        except:
            conn.rollback()
            conn.close()
            msg = "Error..! couldn't insert the details into the database."
        finally:
            return render_template("result.html", msg=msg)


@app.route('/login_validation', methods=['POST'])
def login_validation():
    """It checks user details with details stored in the database.
       If the username and password is existed in the database
       then it navigates to the w3 schools page.
       Otherwise, register page is displayed to register.
    """
    user_name = request.form['user_name']
    password = request.form['password']
    conn = mysql.connector.connect(host="localhost", user="root", database="flaskapp")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM user_details WHERE user_name=(%s) AND password=(%s)""", (user_name, password))
    row = cursor.fetchall()
    if len(row) <= 0:
        return render_template('registration_page.html')
    else:
        # user_details = cursor.execute("""SELECT * FROM user_details WHERE user_name=(%s)""", [user_name])
        return render_template("success_page.html", user_details=row)
    conn.close()


app.run(debug=True)
