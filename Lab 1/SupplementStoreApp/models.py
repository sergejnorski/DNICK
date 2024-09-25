from django.db import models

# Create your models here.


# Секој суплемент се карактеризира со име, слика, шифра, производител, достапност(boolean),
# цена, категорија (proteins, vitamins, creatines, amino acids, pre-workout ) и цена.
class Supplement(models.Model):
    CATEGORIES = [
        ('PR', 'PROTEIN'),
        ('VT', 'VITAMINS'),
        ('CR', 'CREATINE'),
        ('AA', 'AMINO-ACID'),
        ('PW', 'PRE-WORKOUT')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    code = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    price = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORIES)