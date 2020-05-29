from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'json_view'
router = routers.DefaultRouter()
router.register('Employees', views.EmployeeView)
urlpatterns = [
    path('', include(router.urls))
]