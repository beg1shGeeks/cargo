from django.db import models

from django.db import models


class Car(models.Model):
    car_number = models.CharField(max_length=100)
    type_car = models.CharField(max_length=100)
    number_license = models.CharField(max_length=150)
    photo_car = models.ImageField(blank=True)
    insurance = models.BooleanField(max_length=50)

    def __str__(self):
        return self.car_number


class Phone_number(models.Model):
    number = models.IntegerField()



class Driver(models.Model):
    CHOICE = (
        ('Individual', 'Individual'),
        ('Entity', 'Entity')
    )
    name = models.CharField(max_length=40, name='driver_name')
    surname = models.CharField(max_length=40, name='driver_surname')
    telephone_number = models.ForeignKey(Phone_number, on_delete=models.CASCADE)
    email_driver = models.EmailField(max_length=100)
    face = models.CharField(choices=CHOICE, max_length=100, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

