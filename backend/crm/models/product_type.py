from django.db import models


class ProductType(models.Model):
    type_name = models.CharField(max_length=10)