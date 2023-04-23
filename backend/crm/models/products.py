from django.db import models
from .product_type import ProductType


class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
