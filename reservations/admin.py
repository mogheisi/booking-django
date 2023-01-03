from django.contrib import admin
from residences.models import City, Country, Amenity
from reservations.models import HotelBooking

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Amenity)
admin.site.register(HotelBooking)
