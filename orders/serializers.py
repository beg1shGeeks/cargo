from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import (
    Orders
)


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderValidateSerialiser(serializers.Serializer):
    cargo_name = serializers.CharField(required=True)
    cargo_weight = serializers.CharField(required=True)
    cargo_value = serializers.CharField(required=True)
    sending_date = serializers.DateField(required=True)
    loading_location = serializers.CharField(required=True)
    loading_time = serializers.TimeField(required=True)
    unloading_place = serializers.CharField(required=True)
    unloading_time = serializers.TimeField(required=True)
    car_box = serializers.CharField(required=True)
    loading_car = serializers.CharField(required=True)
    unloading_car = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)

