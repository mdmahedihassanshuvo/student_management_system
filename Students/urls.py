from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView,
    StudentDetailsView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    path(
        'student_list/',
        StudentListView.as_view(),
        name='student_list'
    ),
    path(
        'student_create/',
        StudentCreateView.as_view(),
        name='create_student'
    ),
    path(
        'student_details/<int:student_id>/',
        StudentDetailsView.as_view(),
        name='student_details'
    ),
    path(
        'student_update/<int:student_id>/',
        StudentUpdateView.as_view(),
        name='update_student'
    ),
    path(
        'student_delete/<int:student_id>/',
        StudentDeleteView.as_view(),
        name='student_delete'
    )
]
