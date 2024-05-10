from django.contrib import admin

# Register your models here.
from .models import Customer, Driver, BookRide

admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(BookRide)

