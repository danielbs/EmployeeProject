from django.contrib import admin
from .models import Employee, Manager, Job, Department

admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Job)
admin.site.register(Department)