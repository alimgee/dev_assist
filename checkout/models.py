from django.db import models
from django.contrib.auth.models import User # built in django user table
from donation.models import Donation

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)