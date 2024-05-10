# Generated by Django 5.0.3 on 2024-05-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rides', '0010_bookride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookride',
            name='ride_status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('booked', 'Booked'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='waiting', max_length=20),
        ),
    ]
