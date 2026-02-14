from django.shortcuts import render
from .models import Teacher
# Create your views here.

def teacher_details(request):
    teacher= Teacher.objects.all()
    return render(request, 'teacher_details.html', {'teacher':teacher})

def home(request):
    return render(request, 'home.html')
