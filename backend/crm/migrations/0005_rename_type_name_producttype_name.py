# Generated by Django 4.2 on 2023-04-23 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_orderstatus_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='type_name',
            new_name='name',
        ),
    ]