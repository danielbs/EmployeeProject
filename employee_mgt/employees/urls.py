from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'employees'
urlpatterns = [
    path('', views.employee_list, name='list'),
    path('<int:emp_id>/', views.employee_detail, name='employee_detail'),
]
