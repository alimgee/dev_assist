from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from checkout.forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from donation.models import Donation
import stripe
from django.contrib.auth.decorators import login_required

# taking stripe api key from env settings
stripe.api_key = settings.STRIPE_SECRET


# user must be logged in to see checkout
@login_required
def checkout(request):
    user = request.user
    # if user fills in forms on checkout
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # check if forms are valid
        if order_form.is_valid() and payment_form.is_valid():
            # add current date and user to form and save
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = user
            order.save()
            # get cart content once checkout details are submitted correctly
            cart = request.session.get('cart', {})
            total = 0
            # finding cart donation types and calculating overall price
            for id, quantity in cart.items():
                donation = get_object_or_404(Donation, pk=id)
                total += quantity * donation.price
                # adding order to db
                order_line_item = OrderLineItem(
                    order=order,
                    donation=donation,
                    quantity=quantity
                    )
                order_line_item.save()

            try:
                # processing stripe payment
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            # display card errors if any
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            # if payment is successful empty cart content and inform user
            if customer.paid:
                messages.success(request, f'You have successfully paid')
                request.session['cart'] = {}
                return redirect(reverse('donations'))
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(payment_form.errors)
            messages.error(request,
                           "We were unable to take a payment with that card!")

    else:
        # loading payment forms
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    context={
        'title':'Checkout'
    }
    return render(request, "checkout/checkout.html", context,
                  {'order_form': order_form, 'payment_form': payment_form,
                   'publishable': settings.STRIPE_PUBLISHABLE})
