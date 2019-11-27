from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from checkout.forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from donation.models import Donation
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    payment_form = MakePaymentForm()
    order_form = OrderForm()
        
    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
