from django.db import models


class ProductUnit(models.Model):
    unit = models.CharField(max_length=10, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Едиинцы измерения'

    def __str__(self):
        return self.unit
