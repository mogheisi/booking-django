from django.contrib import admin
from .models import Hotel, Room


class ModelInLine(admin.StackedInline):
    model = Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = (ModelInLine,)


admin.site.register(Room)

