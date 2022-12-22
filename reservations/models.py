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


class Facility(models.Model):
    facility_title = models.CharField(max_length=32)
    facility_description = models.TextField()
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.facility_title
