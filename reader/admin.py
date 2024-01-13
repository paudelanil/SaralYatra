from django.contrib import admin
from .models import Read,Passenger,NFCData,BusData

# Register your models here.
admin.site.register(Read)

admin.site.register(Passenger)

admin.site.register(NFCData)
admin.site.register(BusData)