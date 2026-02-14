from django.shortcuts import render
from .models import Students, Teacher, Courses

# Create your views here.

def student_list(request):
    students = Students.objects.all()
    return render(request, 'school/student_list.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'school/course_list.html', {'courses': courses})
