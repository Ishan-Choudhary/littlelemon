# Generated by Django 5.0.6 on 2024-06-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menutable_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutable',
            name='Inventory',
            field=models.PositiveIntegerField(),
        ),
    ]
