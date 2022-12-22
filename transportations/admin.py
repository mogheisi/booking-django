from django.contrib import admin
from .models import FlightTicket, Airline, FlightPrice


admin.site.register(Airline)


class ModelInLine(admin.StackedInline):
    model = FlightPrice


@admin.register(FlightTicket)
class FlightTicketAdmin(admin.ModelAdmin):
    inlines = (ModelInLine,)
