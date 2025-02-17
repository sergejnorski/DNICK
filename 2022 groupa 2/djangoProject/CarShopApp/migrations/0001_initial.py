# Generated by Django 5.0.3 on 2024-06-06 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('max_speed', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year_of_starting', models.IntegerField()),
                ('fixes_oldtimers', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website_link', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description_of_problem', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarShopApp.car')),
                ('car_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarShopApp.carshop')),
            ],
        ),
        migrations.CreateModel(
            name='CarShopManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarShopApp.carshop')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarShopApp.manufacturer')),
            ],
        ),
    ]
