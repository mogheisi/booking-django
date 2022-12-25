from django.db import models
from residences.models import City, Amenity
from comments.models import AbstractComment


# class FlightType(models.Model):
#     type_title = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.type_title


class Airline(models.Model):
    title = models.CharField(max_length=32)
    #  rate
    #  comments

    def __str__(self):
        return self.title


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    airport_name = models.CharField(max_length=32)


class AbstractTransportationTicket(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination')
    capacity = models.IntegerField()
    amenities = models.ForeignKey(Amenity, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        abstract = True


class FlightTicket(AbstractTransportationTicket):
    flight_number = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def __str__(self):
        return f'flight number {self.flight_number}, {self.airline}'


class FlightTypePrice(models.Model):
    type_choices = (
        ('B', 'Business class'),
        ('F', 'First class'),
        ('E', 'Economy class'),
    )
    flight = models.ForeignKey(FlightTicket, on_delete=models.CASCADE)
    flight_type = models.CharField(choices=type_choices, max_length=1)
    price = models.IntegerField()


class AirlineComment(AbstractComment):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.airline
