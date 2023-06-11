from django.db import models
from .product_type import ProductType
from .unit import ProductUnit


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    unit = models.ForeignKey(ProductUnit, on_delete=models.DO_NOTHING, verbose_name='Единица измерения')
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, verbose_name='Тип')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name
