from rest_framework import serializers
from .models import Employee,Manager,Job,Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id', 'first_name', 'last_name', 'email', 'phone_nr', 'hire_date', 'job_id', 
                    'salary', 'commission_pct', 'manager_id', 'department_id']

