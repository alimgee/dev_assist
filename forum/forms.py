from django import forms
from datetime import datetime
from forum.models import Post, Comment

class QueryForm(forms.ModelForm):
    '''form for sbmitting a new query'''
    title = forms.CharField(
        label="Your Post Title",
        min_length=3,
        max_length=80,
        widget=forms.TextInput(),
        required=True)
    content = forms.CharField(
        label="Post Detail",
        min_length=10,
        max_length=1500,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Post
        fields = ["title", "content"]

class CommentForm(forms.ModelForm):
    '''form for sbmitting a new query'''
    content = forms.CharField(
        label="Comment Detail",
        min_length=10,
        max_length=1500,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Comment
        fields = ["content"]