from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    messages.success(request, f'You have loaded the landing page')
    return render(request, 'index.html') 

def about(request):
    messages.success(request, f'You have loaded the about page')
    return render(request, 'about.html') 
