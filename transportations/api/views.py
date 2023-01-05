from rest_framework import generics

from .serializers import TicketSerializer
from transportations.models import FlightTicket
from transportations.filter import FlightTicketFilterSet


class TicketsView(generics.ListAPIView):
    queryset = FlightTicket.objects.all()
    serializer_class = TicketSerializer
    filterset_class = FlightTicketFilterSet
