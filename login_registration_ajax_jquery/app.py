from flask import Flask, render_template, request, jsonify, redirect
import mysql.connector
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

# Creating a secret key
app.secret_key = "caircocoders-ednalan"

# Connecting to the database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def login():
    """Displays login form."""
    return render_template("login_form.html")


@app.route('/register/')
def register():
    """Displays registration form."""
    return render_template("registration_form.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    """
    Compares user entered details with details in the database.
    If matches records else error message is displayed.
    """
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM user_info WHERE email LIKE (%s) AND password LIKE (%s)""", (email, password))
    users = cursor.fetchall()
    print(users)
    if len(users) > 0:
        #return redirect("/index")
        return index()
    else: 
        message = "please register before login"
        return render_template("login_form.html", msg=message)
    

@app.route('/add_user', methods=["POST"])
def add_user():
    """
    It takes details from the user and records are displayed 
    if successfully details are stored in the database.
    """
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    name = request.form.get('name')
    email = request.form.get('email')
    ph_no = request.form.get('ph_no')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM user_info WHERE email LIKE %s""", [email])
    record = cursor.fetchall()
    if len(record)>=1:
        msg = "This email is already in use. Register with another Email"
        return render_template("registration_form.html", msg=msg)
    else:
        cursor.execute("""INSERT INTO user_info (name, email, phone_no, password) VALUES (%s, %s, %s, %s)""",
                    (name, email, ph_no, password))
        mysql.connection.commit()
        #return redirect("/index")
        return index()


def index():
    """Displays records in the database in the ascending order of id."""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM user_info ORDER BY id")
    employee = cur.fetchall()
    return render_template('index.html', employee=employee)


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    """get the user entered details from the form and add
     those details to the database """

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # getting user entered details using the name attribute from the form
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtemail = request.form['txtemail']
        txtphone = request.form['txtphone']
        txtpwd = request.form['txtpwd']
        # print(txtname)
        # if the form details are empty show the text to enter details
        if txtname == '':
            msg = 'Please Input Name'
        elif txtemail == '':
            msg = 'Please Input Email ID'
        elif txtphone == '':
            msg = 'Please Input Phone Number'
        elif txtpwd == '':
            msg = 'Please Input Password'
        else: 
            cur.execute("""SELECT * FROM user_info WHERE email LIKE %s""", [txtemail])
            record = cur.fetchall()
            if len(record)>=1:
                msg = "This email is already in use. Register with another Email"
                
            else:                     
                cur.execute("INSERT INTO user_info (name, email, phone_no, password) VALUES (%s, %s, %s, %s)",
                            [txtname, txtemail, txtphone, txtpwd])
                mysql.connection.commit()       
                cur.close()
                msg = 'New record created successfully'
    return jsonify(msg)


@app.route("/ajax_update", methods=["POST", "GET"])
def ajax_update():
    """Edit the record of the details with new details in the database."""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtemail = request.form['txtemail']
        txtphone = request.form['txtphone']
        txtpwd = request.form['txtpwd']
        print("String is: " + str(string))
        cur.execute("""SELECT * FROM user_info WHERE email LIKE %s""", [txtemail])
        record = cur.fetchall()
        print("Edit: " + str(record))
        if len(record) > 0:
            msg = "This Email is already in use. Please update with another Email."
        else:
            cur.execute("UPDATE user_info SET name = %s, email = %s, phone_no = %s, password = %s WHERE id = %s ",
                        [txtname, txtemail, txtphone, txtpwd, string])
            mysql.connection.commit()       
            cur.close()
            msg = 'Record is Successfully Updated.'
    return jsonify(msg)    


@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    """Delete the record in the database taking id value."""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        id = request.form['string']
        print(id)
        cur.execute("""DELETE FROM user_info WHERE id = (%s)""", [id])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record is Deleted Successfully.'
    return jsonify(msg) 
 

app.run(debug=True)
