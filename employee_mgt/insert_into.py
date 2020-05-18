import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dbash@2911",
    database = "acme_db"
)

mycursor = mydb.cursor()

dptFormula = "INSERT INTO employees_department (department_name) VALUES (%s)"
acme_departments = [("Accounting",),("R&D",),("Support",)]
mycursor.executemany(dptFormula, acme_departments)

jobFormula = "INSERT INTO employees_job (job_name) VALUES (%s)"
acme_jobs = [("Accountant",),("Developer",),("Team Leader",),("Support Specialist",)]
mycursor.executemany(jobFormula, acme_jobs)

mngFormula = "INSERT INTO employees_manager (employee_id) VALUES (%s)"
acme_managers = [(100,),(101,),(102,)]
mycursor.executemany(mngFormula, acme_managers)
mydb.commit()
