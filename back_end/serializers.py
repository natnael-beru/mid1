from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Student_information
from .models import teacher
from .models import employee


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_information
        fields = '__all__'


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
