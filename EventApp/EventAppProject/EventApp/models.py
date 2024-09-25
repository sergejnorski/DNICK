from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_establishment = models.DateField()
    number_of_events = models.IntegerField()


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    poster = models.ImageField(upload_to='event_posters', null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    open_air = models.BooleanField(default=False)


class BandEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
