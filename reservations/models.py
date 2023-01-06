from django.db import models
from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from transportations.models import FlightTicket
from residences.models import Hotel, Room


class AbstractReserve(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    reservation_number = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class FlightTicketReservation(AbstractReserve):
    flight = models.ForeignKey(FlightTicket, on_delete=models.PROTECT)
    id_number = models.IntegerField(unique=True)


class HotelBooking(AbstractReserve):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)

