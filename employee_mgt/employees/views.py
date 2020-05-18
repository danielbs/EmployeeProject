from rest_framework import viewsets,permissions
from .models import Employee,Manager,Department,Job
from .serializers import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
