from django.contrib import admin
from .models import FlightTicket, Airline


admin.site.register(FlightTicket)
admin.site.register(Airline)
