from django.urls import path

from .views import HotelView

urlpatterns = [
    path('hotelbooking/', HotelView.as_view())
]
