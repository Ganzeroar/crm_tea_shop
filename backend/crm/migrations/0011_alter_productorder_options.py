# Generated by Django 4.2 on 2023-05-09 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_remove_orders_product_orders_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productorder',
            options={'verbose_name': 'Один заказ', 'verbose_name_plural': 'Конкретные заказы'},
        ),
    ]
