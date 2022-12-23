from django.db import models
from residences.models import City, Amenity
from comments.models import AbstractComment


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


class AbstractTransportationTicket(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination')
    capacity = models.IntegerField()
    amenities = models.ForeignKey(Amenity, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class FlightTicket(AbstractTransportationTicket):
    flight_number = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)

    def __str__(self):
        return f'flight number {self.flight_number}, {self.airline}'


class FlightPrice(models.Model):
    flight = models.ForeignKey(FlightTicket, on_delete=models.CASCADE)
    flight_type = models.ForeignKey(FlightType, on_delete=models.CASCADE)
    price = models.IntegerField()


class AirlineComment(AbstractComment):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.Airline
