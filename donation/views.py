from django.shortcuts import render
from donation.models import Donation

# Create your views here.
def donations(request):
    donations = Donation.objects.all()
    context = {
        
        "donations": donations,
        "title" : 'Donations'
    } 
    return render(request, 'donation/donation.html', context ) 