from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView
)

urlpatterns = [
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_create/', StudentCreateView.as_view(), name='create_student')
]
