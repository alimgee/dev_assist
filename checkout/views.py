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
    user =request.user

    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = user
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                donation = get_object_or_404(Donation, pk=id)
                total += quantity * donation.price
                order_line_item = OrderLineItem(
                    order = order, 
                    donation = donation, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.success(request, f'You have successfully paid')
                request.session['cart'] = {}
                return redirect(reverse('donations'))
            else:
                messages.error(request, "Unable to take payment")
                
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
            
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


