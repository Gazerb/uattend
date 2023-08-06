# External Imports
from django.shortcuts import render
from .models import Students, Grades, Attendance 

# Internal Imports
from . import views


def all_students(request):
    """A view to load student page"""

    students = Students.objects.all()
    grades = Grades.objects.all()
    attendance = Attendance.objects.all()

    context = {
        'students' : students,
        'grades' : grades,
        'attendance' : attendance,
    }

    return render(request, "students/students.html", context)