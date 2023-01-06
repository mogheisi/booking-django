from django.urls import path

from .views import HotelPaymentAPIView


urlpatterns = [
    path('pay/<int:pk>/', HotelPaymentAPIView.as_view()),
]
