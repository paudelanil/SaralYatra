from django.urls import path
from .views import HomePageView,initalProfile,scan_passenger

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("initialProfile/",initalProfile,name = 'initalProfile'),
    path("passenger_details/",scan_passenger,name= 'passenger_details'),
]
