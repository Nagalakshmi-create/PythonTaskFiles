import sqlite3

conn = sqlite3.connect('database.db')
print('opened')
conn.execute(""" CREATE TABLE details(name VARCHAR(255) ,email CHAR(25) ,contact varchar(255),password varchar(255))""")
print('Table created')
conn.close()
