from django.urls import path
from .views import (
    initialProfile,
    getDetails,
    passenger_tapped,
    save_nfc_data,
    adminPage,
    busdata,
)

urlpatterns = [
    path("", getDetails, name="home"),
    path("initialProfile/", initialProfile, name="initialProfile"),
    path("passenger_tapped/<int:id>/", passenger_tapped, name="passenger_tapped"),
    path("save_nfc_data/", save_nfc_data, name="passenger_tapped"),
    path("adminPage/", busdata, name="busdata"),
    path("adminPage/", adminPage, name="adminPage"),
]
