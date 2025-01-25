from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render the home.html template

def about(request):
    return render(request, 'about.html')  # Render the about.html template
