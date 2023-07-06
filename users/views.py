from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from users.serializers import UserValidateSerializer, UserCreateSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        user = User.objects.create_user(**serializer.validated_data)
        return Response(data={'user_id': user.id})

@api_view(['POST'])
def authoriation_api_view(request):
    if request.method == 'POST':
        serializer = UserValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        user = authenticate(**serializer.validated_data)

        @receiver(post_save, sender=settings.AUTH_USER_MODEL)
        def create_auth_token(sender, instance=None, created=False, **kwargs):
            if created:
                Token.objects.create(user=instance)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Неверные учетные данные'}, status=400)