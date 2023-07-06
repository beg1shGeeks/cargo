from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise ValidationError('Пользователь с таким именем уже существует')
        except User.DoesNotExist:
            return username
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)