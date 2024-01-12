from django.urls import path
from .views import HomePageView, initialProfile, getDetails,tap_passenger,passenger_tapped

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("initialProfile/", initialProfile, name='initialProfile'),
    path("getDetails/", getDetails, name='getDetails'),
    path("tap_passenger/", tap_passenger, name='tap_passenger'),
    path("passenger_tapped/<int:id>/", passenger_tapped, name='passenger_tapped'),
    # path("passenger_details/<int:id>", detail_page, name='passenger_details'),
]
