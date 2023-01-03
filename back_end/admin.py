from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(teacher)
admin.site.register(employee)
admin.site.register(Student_information)