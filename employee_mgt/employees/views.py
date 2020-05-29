from rest_framework import viewsets,permissions
from .models import Employee,Manager,Department,Job
from .serializers import EmployeeSerializer
from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def employee_list(request):
    employees = Employee.objects.all()
    managers = Manager.objects.all()
    departments = Department.objects.all()
    jobs = Job.objects.all()
    return render(request, 'employees/employee_list.html', {'employees':employees})

def employee_detail(request,emp_id):
    employee  = Employee.objects.get(emp_id=emp_id)
    managers = Manager.objects.all()
    departments = Department.objects.all()
    jobs = Job.objects.all()
    return render(request, 'employees/employee_detail.html', {'employee':employee, 'managers':managers, 'departments':departments, 'jobs':jobs})
