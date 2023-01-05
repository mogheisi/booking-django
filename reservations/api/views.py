from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from residences.api.serializers import HotelSerializer
from residences.models import Hotel, Room
from transportations.models import FlightTicket
from transportations.api.serializers import TicketSerializer
from reservations.api.serializers import HotelBookingSerializer, FlightTicketReserveSerializer


class HotelBookingAPIView(APIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        hotel = Hotel.objects.get(id=pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = HotelBookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            room = Room.objects.get(id=request.data['room'])
            room.status = '1'
            room.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightTicketReservationAPIView(APIView):

    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        flight = FlightTicket.objects.get(flight_number=pk)
        serializer = TicketSerializer(flight)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = FlightTicketReserveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            flight = FlightTicket.objects.get(flight_number=pk)
            flight.capacity -= 1
            flight.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
