from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Секој бенд се карактеризира со име, име на држава од каде потекнува, година на формирање и број на одржани настапи.
# Бендовите може да настапуваат на повеќе настани.
class Band(models.Model):
    def __init__(self, name):
        self.ime = name

    ime = models.CharField(max_length=100, null=True, blank=True)
    imeDrzava = models.CharField(max_length=100, null=True, blank=True)
    godinaFormiranje = models.IntegerField(null=True, blank=True)
    brojOdrzaniNastani = models.IntegerField(null=True, blank=True)


# Секој настан се карактеризира со име, датум и време на одржување на настанот,
# постер, корисник кој го креирал настанот, бендови кои настапуваат на настанот,
# информација дали настанот е на отворено или не.
class Event(models.Model):
    def __init__(self, name):
        self.ime = name

    ime = models.CharField(max_length=100)
    vremeOdrzuvanje = models.DateField(null=True, blank=True)
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    kreator = models.ForeignKey(User, on_delete=models.CASCADE)
    bendovi = models.CharField(max_length=255, null=True, blank=True)
    daliENaOtvoreno = models.BooleanField(null=True, blank=True)


class BandEvent(models.Model):
    bands = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
