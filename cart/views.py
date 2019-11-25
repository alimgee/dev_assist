from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart/cart.html")
