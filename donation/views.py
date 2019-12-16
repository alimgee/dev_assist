from django.shortcuts import render
from donation.models import Donation


# view for donation page
def donations(request):
    '''
    function to get all donation objects in db
    and pass to template for display
    '''
    donations = Donation.objects.all()
    context = {
        "donations": donations,
        "title": 'Donations'
    }
    return render(request, 'donation/donation.html', context)
