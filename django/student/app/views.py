from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')

    return render(request, 'add_student.html', {'form': form})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')

    return render(request, 'update_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('view_students')


