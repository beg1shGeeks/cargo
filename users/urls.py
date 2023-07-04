from django.urls import path
from users import views


urlpatterns = [
    path('authoriation/', views.authoriation_api_view),
    path('registration/', views.registration_api_view),
]

