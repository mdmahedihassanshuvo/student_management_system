# from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView
)
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/create.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        return super().form_valid(form)
