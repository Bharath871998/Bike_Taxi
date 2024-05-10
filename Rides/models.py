from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone



class Customer(models.Model):
    username = models.CharField(max_length=50, blank=True, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Driver(models.Model):
    username = models.CharField(max_length=50, blank=True, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12, unique=True)
    driving_license = models.CharField(max_length=10, unique=True)
    vehicle_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class BookRide(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='rides')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_rides')
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    time_of_booking = models.DateTimeField(default=timezone.now)
    ride_status = models.CharField(max_length=20, choices=[
        ('waiting', 'Waiting'),
        ('ride accepted', 'Ride Accepted'),
        ('in_progress', 'In Progress'),
        ('ride ended', 'Ride Ended'),
        ('ride cancelled', 'Ride Cancelled')
    ], default='waiting')

    def __str__(self):
        return f"{self.customer.username} from {self.source} to {self.destination}"
