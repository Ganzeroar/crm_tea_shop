# Generated by Django 4.2 on 2023-04-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_remove_orders_quantity_alter_orders_id_productorder_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ManyToManyField(to='crm.productorder', verbose_name='Продукт'),
        ),
    ]
