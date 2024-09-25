from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# За секој пилот се чуваат негово име и презиме, година на раѓање
# вкупно часови налет и чин кој го има во компанијата.
class Pilot(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    number_of_fly_hours = models.IntegerField()
    company_title = models.CharField(max_length=100)


# За секој балон се чуваат типот на балонот, име на производителот на
# балонот и максимален дозволен број на патници во балонот.
class Balloon(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()


# За авиокомпанијата се чува нејзиното име,
# година на основање и информација дали лета надвор од Европа или не.
class Airline(models.Model):
    name = models.CharField(max_length=100)
    date_of_creation = models.DateField()
    does_fly_outside_of_Europe = models.BooleanField()


# Секој лет се карактеризира со задолжителна шифра, име на кој аеродром полетува и на кој
# аеродром слетува, корисник кој го креирал летот, фотографија за летот, информација со кој
# балон се изведува летот, пилот на летот и авиокомпанија која го реализира летот
class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    airport_from = models.CharField(max_length=100)
    airport_to = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)


# Дополнително, за секоја авиокомпанија се чува информација за пилотите со кои
# соработува. Еден пилот може да биде соработник на повеќе авиокомпании.
class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)