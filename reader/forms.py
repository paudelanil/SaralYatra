from django import forms
from .models import Passenger


class PassengerForm(forms.Form):
    passenger_id = forms.IntegerField(label="Passenger ID")
