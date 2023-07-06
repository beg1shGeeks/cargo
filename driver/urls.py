from django.urls import path
from driver.views import CarApiView, DriverApiView, PhoneNumberApiView, CarDetailAPIView, PhoneDetailApiView, DriverDetailApiView

urlpatterns = [
    path('cars/', CarApiView.as_view()),
    path('cars/<int:id>', CarDetailAPIView.as_view()),
    path('driver/', DriverApiView.as_view()),
    path('driver/<int:id>', DriverDetailApiView.as_view()),
    path('phone_number/', PhoneNumberApiView.as_view()),
    path('phone_number/<int:id>', PhoneDetailApiView.as_view())
]
