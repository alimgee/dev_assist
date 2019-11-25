from django.shortcuts import render, redirect, reverse

def view_cart(request):
    '''A View that renders the cart contents page'''
    context={
        'title':'Cart'
    }
    return render(request, "cart/cart.html", context)

def add_to_cart(request, id):
    '''Add a donation item to the cart'''
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))

