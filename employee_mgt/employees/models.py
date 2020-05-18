from django.db import models


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.job_name

class Manager(models.Model):
    mgr_id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField()
    def __str__(self):
        return str(self.employee_id)

class Department(models.Model):
    dpt_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length = 250)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=70)
    phone_nr = models.CharField(max_length = 25)
    hire_date = models.DateField()
    job_id = models.ForeignKey(Job, on_delete=models.DO_NOTHING)
    salary = models.FloatField()
    commission_pct = models.FloatField()
    manager_id = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name+ ' employee number: ' + str(self.emp_id)
