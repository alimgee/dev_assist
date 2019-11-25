from django.shortcuts import get_object_or_404
from donation.models import Donation


def cart_contents(request):
    '''
    Ensures that the cart contents are available when rendering
    every page
    '''
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    donation_count = 0
    
    for id, quantity in cart.items():
        donation = get_object_or_404(Donation, pk=id)
        total += quantity * donation.price
        donation_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'donation': donation})
    
    return {'cart_items': cart_items, 'total': total, 'donation_count': donation_count}