from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # built in django user table
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # cascade -  when user is deleted remove all posts

    class Meta:
        ordering = ("-date_posted", )

    def __str__(self):
        return self.title # will return the title in the shell view    

  
class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    query = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


