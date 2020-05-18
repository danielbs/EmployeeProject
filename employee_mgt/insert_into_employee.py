import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dbash@2911",
    database = "acme_db"
)

mycursor = mydb.cursor()

empFormula = """INSERT INTO employees_employee (
            first_name, last_name, email, phone_nr, hire_date, job_id_id, salary, 
            commission_pct, manager_id_id, department_id_id)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
acme_employees = [("Daniel","Ben-Shabtay","daniel@benshabtay.com","0526710299","2000-10-05",1,10000.00,25.00,1,4),
                    ("Shaked","Efraim","shakedefraim@gmail.com","0546716289","2010-11-25",1,11000.00,26.00,1,5),
                    ("Alex","Kuznetsov","kalex7878@gmail.com","0516714281","2009-08-15",1,21000.00,27.00,2,5),
                    ("Tsahi","Friedman","tsahifridman@gmail.com","0528714280","2012-01-15",1,13000.00,26.00,3,6),
                    ("Liad","Young","liad64@gmail.com","0536326269","2015-12-14",1,12000.00,26.00,2,5),
                    ("Kadan","Law","kadan1993@gmail.com","0523615289","2010-11-25",1,11000.00,26.00,1,4),
                    ("Yotam","Gil","yotigil@gmail.com","0505714359","2010-11-25",1,11000.00,26.00,1,6),
                    ("Gil","Yotam","mimrahonet@gmail.com","0525415279","2010-11-25",1,11000.00,26.00,3,5),
                    ("Baruch","Snir","baruchsnir@hotmail.com","0536712281","2010-11-25",1,11000.00,26.00,1,6),
                    ("Eliran","Alon","eliranalon1983@gmail.com","0505416383","2010-11-25",1,11000.00,26.00,1,4),
                    ("Yuval","Raz","familyraz@gmail.com","0535711309","2020-01-08",1,12000.00,30.00,2,5)]
mycursor.executemany(empFormula, acme_employees)

mydb.commit()
