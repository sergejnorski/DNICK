from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pilot(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    yearOfBirth = models.IntegerField()
    totalFlyHours = models.IntegerField()
    companyStatus = models.CharField(max_length=100)


class Balloon(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    maxPassengers = models.IntegerField()


class Airline(models.Model):
    name = models.CharField(max_length=100)
    yearOfStart = models.IntegerField()
    fliesOutsideEurope = models.BooleanField()


class AirlinePilot(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)


class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    flightId = models.CharField(max_length=100)
    airportFrom = models.CharField(max_length=100)
    airportTo = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.SET_NULL, null=True, blank=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.SET_NULL, null=True, blank=True)
    airline = models.ForeignKey(Airline, on_delete=models.SET_NULL, null=True, blank=True)
