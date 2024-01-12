from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Read, Passenger
from .forms import PassengerForm

class HomePageView(ListView):
    model = Read
    template_name = "reader/home.html"

def initialProfile(request):
    return render(request, 'reader/initialProfile.html', )

def getDetails(request):
    context = {}
    form = PassengerForm()

    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger_id = form.cleaned_data['passenger_id']
            passenger = get_object_or_404(Passenger, passengerID=passenger_id)
            context['passenger'] = passenger

    context['form'] = form
    return render(request, 'reader/home.html', context)
