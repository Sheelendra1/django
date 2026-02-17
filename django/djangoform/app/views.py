from django.shortcuts import render, redirect

from .forms import UserForm

def user_form_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()

    return render(request, 'form.html', {'form': form})
