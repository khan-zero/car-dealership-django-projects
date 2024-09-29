from django.db import models
from django.db.models import Model


# Create your models here.

class WellcomeHerro(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    background_img = models.ImageField()

class Vehicles(models.Model):
    car_condition = [
        ('brand new', 'Brand New'),
        ('quite new', 'Quite New'),
        ('used', 'Used'),
    ]

    year = models.CharField(max_length=4)
    body = models.CharField(max_length=255)
    manufactor = models.CharField(max_length=255)
    condition = models.CharField(max_length=255, choices=car_condition, default='brand new')
    model = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    kilometers = models.IntegerField()
    horse_power = models.IntegerField()
    transmission = models.CharField(max_length=255, choices=[('manual', 'Manual'), ('automatic', 'Automatic')])

    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    img = models.ImageField()

    def __str__(self):
        return f"{self.manufactor} {self.model} ({self.year})"


class Services(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)


class ClientsReviews(models.Model):
    user_email = models.EmailField()
    full_name = models.CharField(max_length=255)
    message = models.TextField()
    location = models.CharField(max_length=255)


class Partner(models.Model):
    partner_logo = models.ImageField()


class TopBrands(models.Model):
    name = models.CharField(max_length=255)

    #and more in the future...
