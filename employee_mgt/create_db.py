import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dbash@2911"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE acme_db")

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
