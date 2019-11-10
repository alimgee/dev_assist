from django import forms
from datetime import datetime
from forum.models import Post

class QueryForm(forms.ModelForm):
    '''form for sbmitting a new query'''
    title = forms.CharField(
        label="Your Query Title",
        min_length=3,
        max_length=80,
        widget=forms.TextInput(),
        required=True)
    content = forms.CharField(
        label="Query Detail",
        min_length=10,
        max_length=1500,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Post
        fields = ["title", "content"]
   