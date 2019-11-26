from django.db import models
from django.contrib.auth.models import User # built in django user table
from donation.models import Donation

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    donation = models.ForeignKey(Donation, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.donation.name, self.donation.price)