from django.urls import path
from orders import views

urlpatterns = [
    path('orders/', views.OrdersListCreateAPIView.as_view()),
    path('orders/<int:id>/', views.OrderDateilAPIView.as_view()),
]