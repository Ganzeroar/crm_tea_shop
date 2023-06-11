from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название типа товара')

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'

    def __str__(self):
        return self.name
