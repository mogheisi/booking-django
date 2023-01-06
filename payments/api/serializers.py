from rest_framework import serializers

from payments.models import Payment, GuestUser
from reservations.models import HotelBooking, FlightTicketReservation
from users.models import User


class GuestUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestUser
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    count = serializers.CharField()
    discount_code = serializers.CharField()
    other_passengers = GuestUserSerializer(many=True, required=False)

    class Meta:
        model = Payment
        fields = ['count', 'discount_code', 'other_passengers']

    extra_kwargs = {
        'payment_status': {'write_only': True},
        'other_passengers': {'required': False, 'allow_null': True},
        'passengers_count': {'write_only': True},
        'total_discount': {'required': False, 'allow_null': True},
        'user': {'required': False, 'allow_null': True},
    }

    def create(self, validated_data):
        try:
            reservation = HotelBooking.objects.get(
                reservation_number=self.context['pk'])
            price = reservation.room.price
        except:
            reservation = FlightTicketReservation.objects.get(
                reservation_number=self.context['pk'])
            price = reservation.flight.price

        user = reservation.passenger
        validated_data['user'] = user
        validated_data['total_discount'] = 0
        validated_data['total_price'] = price * validated_data['count']
        validated_data.pop('count')
        validated_data.pop('discount_code')
        other_passengers = validated_data.pop('other_passengers')
        for passenger in other_passengers:
            GuestUser.objects.create(**passenger)
        return super(PaymentSerializer, self).create(validated_data)

