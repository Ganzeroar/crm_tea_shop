from django.db import models
from .products import Products
from .clients import Clients
from .order_statuses import OrderStatus


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
