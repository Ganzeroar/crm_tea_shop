from django.db import models
from .products import Products
from .clients import Clients
from .order_statuses import OrderStatus


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name='Продукт')
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, verbose_name='Клиент')
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING, verbose_name='Статус')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return f'Заказ от {self.date_of_creation}'