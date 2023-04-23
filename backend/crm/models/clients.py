from django.db import models
from .city import City
from phonenumber_field.modelfields import PhoneNumberField


class Clients(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    phone = PhoneNumberField(max_length=15)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
