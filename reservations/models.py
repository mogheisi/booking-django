from django.db import models
from django.conf import settings
from transportations.models import FlightTicket
from residences.models import Hotel


class AbstractReserve(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AbstractPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    total_price = models.IntegerField()
    total_discount = models.IntegerField()
    payment_time = models.DateTimeField()
    status_choices = (
        ('S', 'Successful'),
        ('U', 'Unsuccessful'),
        ('P', 'Pending'),
        ('C', 'Canceled'),
    )
    payment_status = models.CharField(choices=status_choices, max_length=1)

    class Meta:
        abstract = True


class FlightTicketReservation(AbstractReserve):
    flight = models.ForeignKey(FlightTicket, on_delete=models.PROTECT)
    passport_number = models.IntegerField()


class HotelBooking(AbstractReserve):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    # from - to -
