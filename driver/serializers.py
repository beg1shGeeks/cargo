from rest_framework import serializers
from driver.models import Driver, Car, Phone_number


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class DriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class PhoneNumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone_number
        fields = '__all__'
