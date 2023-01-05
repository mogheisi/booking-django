from django.urls import path

from .views import HotelBookingAPIView, FlightTicketReservationAPIView


urlpatterns = [
    path('hotelbooking/<int:pk>/', HotelBookingAPIView.as_view()),
    path('ticketreservation/<int:pk>/', FlightTicketReservationAPIView.as_view()),
]
