from django.contrib import admin
from driver.models import (
    Phone_number,
    Car,
    Driver
)

admin.site.register(Phone_number)
admin.site.register(Driver)
admin.site.register(Car)