from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
 
app = Flask(__name__)
       
app.secret_key = "caircocoders-ednalan"
       
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tblemployee ORDER BY id")
    employee = cur.fetchall()
    return render_template('index.html', employee=employee)


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name'  
        elif txtdepartment == '':
            msg = 'Please Input Department'
        elif txtphone == '':
            msg = 'Please Input Phone'
        else:        
            cur.execute("INSERT INTO tblemployee (name,department,phone) VALUES (%s,%s,%s)",[txtname,txtdepartment,txtphone])
            mysql.connection.commit()       
            cur.close()
            msg = 'New record created successfully'   
    return jsonify(msg)


@app.route("/ajax_update",methods=["POST", "GET"])
def ajax_update():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(string)
        cur.execute("UPDATE tblemployee SET name = %s, department = %s, phone = %s WHERE id = %s ", [txtname, txtdepartment, txtphone, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'   
    return jsonify(msg)    


@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cur.execute('DELETE FROM tblemployee WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
    return jsonify(msg) 
 
     
if __name__ == "__main__":
    app.run(debug=True)
