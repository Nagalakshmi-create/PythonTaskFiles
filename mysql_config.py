from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)


'''configure database'''
db = yaml.load(open("db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)   #instance of mysql obj


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #fetch form data
        userdetails = request.form
        name = userdetails["nm"]
        email = userdetails["mail"]

        cur = mysql.connection.cursor()   #post request to make an entry into db
        cur.execute("INSERT INTO userdetails(name, email) Values (%s, %s)", (name, email))
        mysql.connection.commit()     #it saves the changes in db
        cur.close()        #close cursor
        return "Success"
    else:
        return render_template("form.html")


@app.route("/result")
def result():
    cur = mysql.connect.cursor()
    value_store = cur.execute("SELECT * FROM userdetails")
    if value_store > 0:
        user_details = cur.fetchall()

        return render_template("user.html", user_details=user_details)

    else:
        return "No records found"


if __name__ == "__main__":
    app.run(debug=True)