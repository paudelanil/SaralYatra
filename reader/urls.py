from django.urls import path
from .views import  initialProfile, getDetails,passenger_tapped,save_nfc_data,adminPage,busdata

urlpatterns = [
    path("",getDetails, name="home"),
    path("initialProfile/", initialProfile, name='initialProfile'),
    # path("getDetails/", getDetails, name='getDetails'),
   
    path("passenger_tapped/<int:id>/", passenger_tapped, name='passenger_tapped'),
    # path("passenger_details/<int:id>", detail_page, name='passenger_details'),
    path("save_nfc_data/", save_nfc_data, name="passenger_tapped"),
    path("adminPage/", busdata, name="busdata"),
    path("adminPage/",adminPage,name = 'adminPage')
]
