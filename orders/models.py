from django.db import models


class Orders(models.Model):
    CHOICE = (
        ('Еврофура', 'Еврофура'),
        ('Jumbo', 'Jumbo'),
        ('Автоцепка', 'Автоцепка'),
        ('Рефрижераторный','Рефрижераторный'),
        ('Изотермический','Изотермический'),
        ('Автоцистерна', 'Автоцистерна')
    )
    cargo_name = models.CharField(max_length=100, null=True)
    cargo_email = models.EmailField(max_length=100, null=True)
    cargo_lastname = models.CharField(max_length=100, null=True)
    cargo_weight = models.CharField(max_length=100, null=True)
    cargo_value = models.CharField(max_length=100, null=True)
    sending_date = models.DateField(null=True)
    loading_location = models.CharField(max_length=400, null=True)
    loading_time = models.TimeField(null=True, blank=True)
    unloading_place = models.CharField(max_length=400, null=True)
    car_box = models.CharField(choices=CHOICE,max_length=400, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.cargo_name
