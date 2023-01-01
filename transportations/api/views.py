from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .serializers import TicketSerializer
from transportations.models import FlightTicket


class TicketAddAPIView(generics.ListCreateAPIView):
    queryset = FlightTicket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightTicket.objects.all()
    serializer_class = TicketSerializer
