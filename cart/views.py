from django.shortcuts import render, redirect, reverse

def view_cart(request):
    '''A View that renders the cart contents page'''
    context={
        'title':'Cart'
    }
    return render(request, "cart/cart.html", context)
