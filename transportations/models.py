from django.db import models
from reservations.models import City, Facility
from django.conf import settings


class FlightType(models.Model):
    type_title = models.CharField(max_length=32)

    def __str__(self):
        return self.type_title


class Airline(models.Model):
    title = models.CharField(max_length=32)
    #  rate
    #  comments

    def __str__(self):
        return self.title


class BaseTransportationTicket(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination')
    price = models.IntegerField()
    capacity = models.IntegerField()
    facilities = models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class FlightTicket(BaseTransportationTicket):
    flight_type = models.ForeignKey(FlightType, on_delete=models.CASCADE)
    flight_number = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)

    def __str__(self):
        return f'flight number {self.flight_number}, {self.airline}'
