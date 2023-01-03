from django.contrib import admin
from django.urls import path
from back_end import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('student_list/', views.student_list.as_view()),
    path('employee-list/', views.EmployeeList.as_view()),
    path('teacher-list/', views.TeacherList.as_view()),
    path('student_update/<int:pk>', views.student_update.as_view()),
]
