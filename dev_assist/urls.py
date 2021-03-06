"""dev_assist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views as user_views
from donation import views as donation_view
from django.contrib.auth import views as auth_views # importing built in loginveiw
from django.conf.urls import (handler404, handler500) # using built in error handler to show 404 and 500 page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', user_views.register, name='register'),
    # using the built in log in view to allow log user in 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # using the built in log out functionality
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('community/', include('forum.urls')),
    path('cart/', include('cart.urls')),
    path('donate/', donation_view.donations, name='donations'),
    path('checkout/', include('checkout.urls')),
    # password reset section
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'
         ),
         name='password_reset'),
     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
