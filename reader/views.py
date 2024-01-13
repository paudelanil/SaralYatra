from django.shortcuts import render,get_object_or_404
# from django.views.generic import ListView
from .models import Read, Passenger,NFCData,BusData
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
# def tap_passenger(request):
    
#     context = {}

#     if request.method == 'POST':
#         form = PassengerForm(request.POST)
#         if form.is_valid():
#             passenger_id = form.cleaned_data['passenger_id']
#             passenger = Passenger.objects.get(passengerID=passenger_id)
#             if passenger.tap_count <1:
           
#             # Existing passenger, increment tap_count and update location2
#                 passenger.tap_count += 1
#                 # passenger.location1 = f"New Location for {passenger_id}"
#                 passenger.location1 = "dhobhighat"
#             else:
#                 passenger.tap_count -= 1
#                 passenger.location2 = "pulchowk"
#                 fare = caluclate_price(passenger.location1,passenger.location2,passenger.IDstatus)
#                 context['fare'] = fare

#             passenger.save()
            
            

#             context['passenger'] = passenger
#             return render(request, 'reader/initialProfile.html', context)

#     else:
#         form = PassengerForm()

#     context['form'] = form
#     return render(request, 'reader/home.html', context)

def passenger_tapped(request, id):
    
    passenger = get_object_or_404(Passenger, passengerID=id)

    context = {
        'passenger': passenger,
    }

    return render(request, 'reader/initialProfile.html', context)


@csrf_exempt
def save_nfc_data(request):
    bus_stops = {
        "Kalanki": 0,
        "Balkhu": 2,
        "Nayabato": 2.82,
        "Dhobighat": 3.2,
        "Ekantakuna": 4.53,
        "Mahalaxmisthan": 5.536,
        "Satdobato": 6.464,
        "Gwarko": 7.65,
        "Balkumari": 8.56,
        "Koteshwor": 11.785,
    }
    context = {}
    if request.method == "POST":
        record_type = request.POST.get("record_type")
        data = request.POST.get("data")
        passenger = Passenger.objects.get(passengerID=data)
        bus = BusData.objects.get(busID=1)

        # Your existing logic for processing NFC data and updating the passenger goes here
        if request.method == "POST":
            record_type = request.POST.get("record_type")
            data = request.POST.get("data")
            passenger = Passenger.objects.get(passengerID=data)
            if passenger.tap_count < 1:
                # Existing passenger, increment tap_count and update location2
                passenger.tap_count += 1
                passenger.location1 = f"{passenger.location1}"
            else:
                passenger.tap_count -= 1
                passenger.location2 = f"{passenger.location2}"
                bus.totalPassengers +=1

                distance = abs(
                    bus_stops[passenger.location1] - bus_stops[passenger.location2]
                )

                if distance <= 5:
                    passenger.Fare = 20
                elif distance <= 10:
                    passenger.Fare = 25
                elif distance <= 15:
                    passenger.Fare = 30
                elif distance <= 20:
                    passenger.Fare = 33
                else:
                    passenger.Fare = 15

                if passenger.IDstatus:
                    passenger.Fare *= 0.6
                bus.totalEarned += passenger.Fare
                bus.totalPassengers += 1

            bus.save()
            passenger.save()

            nfc_data = NFCData.objects.create(record_type=record_type, data=data)
            nfc_data.save()

        # Assuming success, construct a JsonResponse with a success flag and redirect URL
        response_data = {"success": True, "redirect_url": "passenger_tapped/" + data}
        return JsonResponse(response_data)

    # Handling other cases or errors
    return JsonResponse({"success": False, "redirect_url": ""})


def busdata(request):
    alldata = BusData.objects.get(busID=1)

    context = {
        "alldata": alldata,
    }

    return render(request, "reader/adminPage.html", context)