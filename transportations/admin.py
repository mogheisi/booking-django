from django.contrib import admin
from .models import FlightTicket, Airline, FlightTypePrice, Airport


admin.site.register(Airline)
admin.site.register(Airport)


class TypePriceInLine(admin.StackedInline):
    model = FlightTypePrice


class AirportInLine(admin.StackedInline):
    model = FlightTypePrice


@admin.register(FlightTicket)
class FlightTicketAdmin(admin.ModelAdmin):
    inlines = (TypePriceInLine, AirportInLine)
