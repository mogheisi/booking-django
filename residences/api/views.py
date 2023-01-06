from rest_framework import generics

from .serializers import HotelSerializer
from residences.models import Hotel
from residences.filter import HotelFilterSet


class HotelView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filterset_class = HotelFilterSet
