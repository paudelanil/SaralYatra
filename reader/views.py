from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Read,Passenger
from .forms import PassengerForm


# Create your views here.
class HomePageView(ListView):
    model = Read
    template_name = "reader/home.html"

def initalProfile(request):
    
    return render(request,'reader/initalProfile.html',context = None)
def scan_passenger(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger_id = form.cleaned_data['passenger_id']
            passenger = get_object_or_404(Passenger, passengerID=passenger_id)
            return render(request, 'reader/passenger_details.html', {'passenger': passenger})
    else:
        form = PassengerForm()

    return render(request, 'reader/home.html', {'form': form})
