from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('input')
        print(f"User Input: {user_input}")
        return render(request, 'from.html', {'input': user_input})
    return render(request, 'from.html')