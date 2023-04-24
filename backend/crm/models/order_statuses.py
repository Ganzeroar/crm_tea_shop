from django.db import models


class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name