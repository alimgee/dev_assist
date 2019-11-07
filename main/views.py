from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        messages.success(request, f'You are currently logged in as {username}')
        
    return render(request, 'index.html', {'title': 'Home'}) 

def about(request):
    messages.success(request, f'You have loaded the about page')
    return render(request, 'about.html',{'title': 'About'}) 
