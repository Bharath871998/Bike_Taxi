# Generated by Django 5.0.3 on 2024-04-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rides', '0008_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='age',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='gender',
        ),
    ]
