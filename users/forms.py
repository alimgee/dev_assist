from django import forms # built in
from django.contrib.auth.models import User # built in
from django.contrib.auth.forms import UserCreationForm # from built in django

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # creating email field 

    class Meta: # additional metadata for form
        model = User # using built in User model
        fields = ['username', 'email', 'password1', 'password2'] # addtional fields to user model