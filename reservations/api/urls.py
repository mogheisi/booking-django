from django.urls import path

from .views import HotelBookingAPIView


urlpatterns = [
    path('hotelbooking/<int:pk>/', HotelBookingAPIView.as_view())
]
