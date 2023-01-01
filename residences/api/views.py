from rest_framework import generics

from .serializers import HotelSerializer
from residences.models import Hotel


class HotelView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

