from rest_framework import viewsets,permissions
from .models import Employee,Manager,Department,Job
from .serializers import EmployeeSerializer
from django.shortcuts import render

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def index(request):
    return render (request, 'base_layout.html')
