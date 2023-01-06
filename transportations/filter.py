import django_filters

from transportations.models import FlightTicket


class FlightTicketFilterSet(django_filters.FilterSet):
    departing = django_filters.DateFilter(field_name='departure_time', lookup_expr='gte')
    returning = django_filters.DateFilter(field_name='arrival_time', lookup_expr='lt')
    origin = django_filters.CharFilter(field_name='origin__city_name')
    destination = django_filters.CharFilter(field_name='destination__city_name')

    class Meta:
        model = FlightTicket
        fields = ['origin', 'destination']
