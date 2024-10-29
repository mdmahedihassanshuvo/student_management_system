from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    student_id = models.IntegerField(unique=True)
    semester = models.IntegerField()
    department = models.CharField(max_length=50, default='')
    grade = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.student_id})"
