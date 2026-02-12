from django.shortcuts import render

def student_view(request, name):
    context = {
        'student_name': name
    }
    return render(request, 'home.html', context)