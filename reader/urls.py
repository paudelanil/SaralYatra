from django.urls import path
from .views import HomePageView, initialProfile, getDetails

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("initialProfile/", initialProfile, name='initialProfile'),
    path("getDetails/", getDetails, name='getDetails'),
    # path("passenger_details/<int:id>", detail_page, name='passenger_details'),
]
