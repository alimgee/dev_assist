from django import forms # built in
from django.contrib.auth.models import User # built in
from django.contrib.auth.forms import UserCreationForm # from built in django

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # creating email field 

    class Meta: # additional metadata for form
        model = User # using built in User model
        fields = ['username', 'email', 'password1', 'password2'] # addtional fields to user model

    def clean_email(self):
        '''
        Checking for emails addresses that may already exist
        '''
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(
                f"A user with that email address already exists.")
        return email