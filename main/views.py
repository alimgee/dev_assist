from django.shortcuts import render
from django.contrib import messages


# functions to load landing page and about page
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        messages.success(request,
                         f'You are currently logged in as {username}')

    return render(request, 'index.html', {'title': 'Home'})


def about(request):

    return render(request, 'about.html', {'title': 'About'})
