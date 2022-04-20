import sqlite3

conn = sqlite3.connect('login_db.db')
print("Connected")
conn.execute("""CREATE TABLE user_details(user_name VARCHAR(100), email VARCHAR(200), 
                                          phone_no INT, password VARCHAR(100))""")
print("Table is created")
conn.close()
