from django import forms

class PassengerForm(forms.Form):
    passenger_id = forms.IntegerField(label='Passenger ID')