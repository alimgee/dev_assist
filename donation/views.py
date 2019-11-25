from django.shortcuts import render

# Create your views here.
def donations(request):
        
    return render(request, 'donation/donation.html') 