from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# add employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)