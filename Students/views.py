# from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    View
)
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
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


class StudentDetailsView(DetailView):
    model = Student
    template_name = 'students/details.html'
    context_object_name = 'student'

    def get_object(self):
        student_id = self.kwargs.get("student_id")
        return get_object_or_404(
            Student,
            student_id=student_id
        )


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/update.html'
    form_class = StudentForm
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')

    def get_object(self):
        student_id = self.kwargs.get("student_id")
        return get_object_or_404(Student, student_id=student_id)

    def form_valid(self, form):
        return super().form_valid(form)


class StudentDeleteView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, student_id=student_id)
        return render(
            request, 'students/student_delete.html',
            {'student': student}
        )

    def post(self, request, student_id):
        student = get_object_or_404(Student, student_id=student_id)
        student.delete()
        return redirect('student_list')
