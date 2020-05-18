import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dbash@2911",
    database = "acme_db"
)

mycursor = mydb.cursor()

sql_formula = ("CREATE TABLE employee (employee_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                                        "first_name VARCHAR(255),"
                                        "last_name VARCHAR(255),"
                                        "email VARCHAR(255),"
                                        "phone_nr VARCHAR(255),"
                                        "hire_date DATE,"
                                        "job_id INTEGER,"
                                        "salary NUMERIC(8,2),"
                                        "commission_pct NUMERIC(8,2),"
                                        "manager_id INTEGER,"
                                        "department_id INTEGER)")
mycursor.execute(sql_formula)

mycursor.execute("CREATE TABLE jobs (job_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, job VARCHAR(255))")

mycursor.execute("CREATE TABLE managers (manager_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, employee_id INTEGER)")

mycursor.execute("CREATE TABLE departments (department_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, department_name VARCHAR(255))")
