from django.core.validators import MinValueValidator, MaxValueValidator
from comments.models import AbstractComment
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


class Policy(models.Model):
    policy_title = models.CharField(max_length=32)
    policy_description = models.TextField()


class Facility(models.Model):
    facility_title = models.CharField(max_length=32)
    facility_description = models.TextField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.facility_title


class AbstractResidence(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    facilities = models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)


class Hotel(AbstractResidence):
    hotel_name = models.CharField(max_length=32)
    hotel_description = models.TextField()
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    hotel_policies = models.ForeignKey(Policy, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField()
    beds = models.IntegerField()
    room_facilities = models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True)
    capacity = models.PositiveSmallIntegerField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"room {self.room_number}, {self.hotel.hotel_name}"


class HotelComment(AbstractComment):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment_body = models.TextField()

    def __str__(self):
        return f"{self.hotel}: {self.comment_body[:10]}..."
