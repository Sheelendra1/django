from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) # Bind data from request.POST
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'student/student_form.html', {'form': form})

def list_student(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})
