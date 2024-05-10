# Generated by Django 5.0.3 on 2024-04-25 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rides', '0007_alter_customer_mobile_alter_customer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('select', 'Select')], default='Select', max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=12, unique=True)),
                ('driving_license', models.CharField(max_length=10, unique=True)),
                ('vehicle_number', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]