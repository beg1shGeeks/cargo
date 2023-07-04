from django.db import models


class Orders(models.Model):
    cargo_name = models.CharField(max_length=100, null=True)
    cargo_weight = models.CharField(max_length=100, null=True)
    cargo_value = models.CharField(max_length=100, null=True)
    sending_date = models.DateField(null=True)
    loading_location = models.CharField(max_length=400, null=True)
    loading_time = models.TimeField(null=True, blank=True)
    unloading_place = models.CharField(max_length=400, null=True)
    unloading_time = models.TimeField(null=True, blank=True)
    car_box = models.CharField(max_length=400, null=True)
    loading_car = models.CharField(max_length=400, null=True, blank=True)
    unloading_car = models.CharField(max_length=400, null=True, blank=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.cargo_name

