from django.shortcuts import render
from django.contrib.auth.decorators import login_required   

def home(request):
    return render(request,'authapp/forapp.html')

def login_view(request):
    return render(request,'authapp/login.html')

@login_required
def home(request):
    return render(request,'authapp/home.html')