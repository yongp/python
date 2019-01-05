#!/usr/local/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="python",
    passwd="1qaz@WSX",
    database="python_learning"
)
print (mydb)

mydbcursor = mydb.cursor()
#mydbcursor.execute("show databases")
#mydbcursor.execute("show tables")
#mydbcursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
#mydbcursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mydbcursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

for x in mydbcursor:
    print (x)