from django.contrib import admin
from residences.models import City, Country, Facility
from reservations.models import HotelBooking

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Facility)
admin.site.register(HotelBooking)
