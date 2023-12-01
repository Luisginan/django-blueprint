from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import MyModel
from .models import Employee
from .serializers import MyModelSerializer
from .serializers import EmployeeSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

