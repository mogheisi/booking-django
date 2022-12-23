from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=64)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    address = models.TextField()
    # location ==> geolocation


class Amenity(models.Model):
    Amenity_title = models.CharField(max_length=32)
    Amenity_description = models.TextField()
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.Amenity_title


class AbstractResidence(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    facilities = models.ForeignKey(Amenity, on_delete=models.CASCADE, blank=True, null=True)
    # location


class Hotel(AbstractResidence):
    hotel_name = models.CharField(max_length=32)
    hotel_description = models.TextField()
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # policies

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField()
    room_facilities = models.ForeignKey(Amenity, on_delete=models.CASCADE, blank=True, null=True)
    # room_type
    capacity = models.PositiveSmallIntegerField()
    is_valid = models.BooleanField(default=True)
    room_status = (
        ('0', 'empty'),
        ('1', 'full'),
    )
    status = models.CharField(choices=room_status, max_length=1)

    def __str__(self):
        return f"room {self.room_number}, {self.hotel.hotel_name}"




