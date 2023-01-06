from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from reservations.api.serializers import HotelBookingSerializer, FlightTicketReserveSerializer
from reservations.models import HotelBooking, FlightTicketReservation
from .serializers import PaymentSerializer
from payments.models import Payment


class HotelPaymentAPIView(APIView):
    def get(self, request, pk):
        reservation = HotelBooking.objects.get(reservation_number=pk)
        serializer = HotelBookingSerializer(reservation)
        return JsonResponse(serializer.data)

    def post(self, request, pk):
        serializer = PaymentSerializer(data=request.data, context={'request': request, 'pk': pk})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class FlightTicketAPIView(APIView):
#     def get(self, request, pk):
#         reservation = FlightTicketReservation.objects.filter(passenger=request.user).get(reservation_number=pk)
#         serializer = FlightTicketReserveSerializer(reservation)
#         return JsonResponse(serializer.data)
#


        # duration = (reservation.end_date.date() - reservation.start_date.date()).days
