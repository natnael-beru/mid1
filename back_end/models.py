
from django.db import models

# Create your models here.
from django.db import models


class Student_information(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    grade = models.CharField(max_length=40)


class teacher(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    salary = models.CharField(max_length=40)
    
    
class employee(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    salary = models.CharField(max_length=40)

