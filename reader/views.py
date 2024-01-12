from django.shortcuts import render,get_object_or_404
# from django.views.generic import ListView
from .models import Read, Passenger,NFCData
from .forms import PassengerForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# class HomePageView(ListView):
#     model = Read
#     template_name = "reader/home.html"

def initialProfile(request):
    return render(request, 'reader/initialProfile.html' )
def adminPage(request):

    return render(request,'reader/adminPage.html')
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
def tap_passenger(request):
    
    context = {}

    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger_id = form.cleaned_data['passenger_id']
            passenger = Passenger.objects.get(passengerID=passenger_id)
            if passenger.tap_count <1:
           
            # Existing passenger, increment tap_count and update location2
                passenger.tap_count += 1
                # passenger.location1 = f"New Location for {passenger_id}"
                passenger.location1 = "dhobhighat"
            else:
                passenger.tap_count -= 1
                passenger.location2 = "pulchowk"
                fare = caluclate_price(passenger.location1,passenger.location2,passenger.IDstatus)
                context['fare'] = fare

            passenger.save()
            
            

            context['passenger'] = passenger
            return render(request, 'reader/initialProfile.html', context)

    else:
        form = PassengerForm()

    context['form'] = form
    return render(request, 'reader/home.html', context)

def passenger_tapped(request, id):
    
    passenger = get_object_or_404(Passenger, passengerID=id)

    context = {
        'passenger': passenger,
    }

    return render(request, 'reader/initialProfile.html', context)

def caluclate_price(location1,location2,IDstatus):
    distance = calulcate_distance(location1,location2)
    fare = 10 + 2 * distance
    if IDstatus:
        
        fare *= 0.6
    return fare


@csrf_exempt
def save_nfc_data(request):
    context = {}
    if request.method == "POST":
        record_type = request.POST.get("record_type")
        data = request.POST.get("data")
        passenger = Passenger.objects.get(passengerID=data)
        if passenger.tap_count <1:
           
            # Existing passenger, increment tap_count and update location2
            passenger.tap_count += 1
            passenger.location1 = f"New Location for {passenger.passengerID}"
        else:
            passenger.tap_count -= 1
            passenger.location2 = f"Final Location for {passenger.passengerID}"

        passenger.save()

        
        nfc_data = NFCData.objects.create(record_type=record_type, data=data)
        nfc_data.save()
        context['passenger'] = passenger
        return render(request, 'reader/initialProfile.html', context)

        

    
def calulcate_distance(location1,location2):
    if (location1=='dhobhighat'  and location2 =='pulchowk'):
        return 10
