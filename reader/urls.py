from django.urls import path
from .views import  initialProfile, getDetails,tap_passenger,passenger_tapped,save_nfc_data,adminPage

urlpatterns = [
    path("",getDetails, name="home"),
    path("initialProfile/", initialProfile, name='initialProfile'),
    # path("getDetails/", getDetails, name='getDetails'),
    path("tap_passenger/", tap_passenger, name='tap_passenger'),
    path("passenger_tapped/<int:id>/", passenger_tapped, name='passenger_tapped'),
    # path("passenger_details/<int:id>", detail_page, name='passenger_details'),
    path("save_nfc_data/", save_nfc_data, name="passenger_tapped"),
    path("adminPage/",adminPage,name = 'adminPage')
]
