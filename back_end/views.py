from urllib import response
from django.shortcuts import render
from rest_framework import generics
from .serializers import studentSerializer
from .serializers import teacherSerializer
from .serializers import employeeSerializer
from .models import Student_information
from .models import teacher
from .models import employee

# Create your views here.


class student_list(generics.ListCreateAPIView):
    queryset = Student_information.objects.all()
    serializer_class = studentSerializer


class  TeacherList(generics.ListCreateAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer
    
    
class EmployeeList(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer











class student_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_information.objects.all()
    serializer_class = studentSerializer
