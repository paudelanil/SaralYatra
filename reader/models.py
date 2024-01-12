from django.db import models


# Create your models here.
class Read(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
class Passenger(models.Model):
    passengerID = models.IntegerField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    location1 = models.CharField(max_length=255)
    location2 = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)
    IDstatus = models.BooleanField(choices=[(1, 'Valid'), (0, 'Invalid')], default=1)

    def str(self):
        return self.full_name