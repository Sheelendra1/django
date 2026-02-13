from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'app.html')

def student_details(request):
    students = Student.objects.all()
    return render(request, 'student_details.html', {'students': students})