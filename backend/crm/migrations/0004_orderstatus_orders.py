# Generated by Django 4.2 on 2023-04-23 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_city_alter_products_price_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.clients')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.products')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.orderstatus')),
            ],
        ),
    ]
