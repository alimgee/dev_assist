from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UserRegisterForm


def register(request):
    # if user submits registrtion form
    if request.method == 'POST':
        # pass form details to form variable
        form = UserRegisterForm(request.POST)
        # if the form is valid save, message user and redirect to index
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Account created! You can now log in')
            # sending user to login page after registration
            return redirect('login')
    else:
        # if form is not submitted displaying the form
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
