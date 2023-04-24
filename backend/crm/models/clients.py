from django.db import models
from .city import City
from phonenumber_field.modelfields import PhoneNumberField


class Clients(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, verbose_name='Город')
    phone = PhoneNumberField(max_length=15, verbose_name='Телефон')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



    def __str__(self):
        return self.name