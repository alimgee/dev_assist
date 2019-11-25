from django.urls import path, include
from cart.views import view_cart
urlpatterns = [
    path('', view_cart, name='view_cart'),
]