from django.urls import path

from .views import HotelView

urlpatterns = [
    path('hotels/', HotelView.as_view())
]
