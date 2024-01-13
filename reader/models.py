from django.db import models


# Create your models here.
# Create your models here.
class Read(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Passenger(models.Model):
    passengerID = models.IntegerField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    tap_count = models.IntegerField(default=0)
    location1 = models.CharField(max_length=255)
    location2 = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(choices=[(1, "Active"), (0, "Inactive")], default=1)
    IDstatus = models.BooleanField(choices=[(1, "Valid"), (0, "Invalid")], default=1)
    Fare = models.IntegerField(default=0)

    def str(self):
        return self.full_name


class NFCData(models.Model):
    record_type = models.CharField(max_length=255)
    data = models.TextField()

    def __str__(self):
        return self.data


class BusData(models.Model):
    busID = models.IntegerField(primary_key=True, unique=True, default=1)
    totalEarned = models.IntegerField(default=0)
    totalPassengers = models.IntegerField(default=0)