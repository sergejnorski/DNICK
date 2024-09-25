from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Car(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=50)


class CarShop(models.Model):
    name = models.CharField(max_length=50)
    year_of_starting = models.IntegerField()
    fixes_oldtimers = models.BooleanField(default=False)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website_link = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)


class Fix(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    date = models.DateField()
    description_of_problem = models.TextField()
    car_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_shop = models.ForeignKey(CarShop, on_delete=models.CASCADE)


class CarShopManufacturer(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    car_shop = models.ForeignKey(CarShop, on_delete=models.CASCADE)
