import django_filters

from residences.models import Hotel


class HotelFilterSet(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='city__city_name__iexact')
    departing = django_filters.DateFilter(field_name='start_time', lookup_expr='gte')
    returning = django_filters.DateFilter(field_name='end_time', lookup_expr='lt')

    class Meta:
        model = Hotel
        fields = ['city']
