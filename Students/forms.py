from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'student_id',
            'semester',
            'department',
            'grade',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':
                    'Enter student name'
                }
            ),
            'student_id': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter student ID'
                }
            ),
            'semester': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter semester'
                }
            ),
            'department': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter department'
                }
            ),
            'grade': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter grade (e.g., 3.75)'
                }
            ),
        }

        help_texts = {
            'name': 'Full name of the student.',
            'student_id': 'Unique student identification number.',
            'semester': 'Current semester number.',
            'department': 'Department of the student.',
            'grade': 'Grade achieved (optional).',
        }
