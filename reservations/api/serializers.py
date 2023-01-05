from rest_framework import serializers

from reservations.models import HotelBooking, FlightTicketReservation
from residences.models import Room
from transportations.models import FlightTicket


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room

        fields = ['room_number']

        extra_kwargs = {
            'hotel': {'required': False, 'allow_null': True},
            'price': {'required': False, 'allow_null': True},
            'room_facilities': {'required': False, 'allow_null': True},
            'capacity': {'required': False, 'allow_null': True},
            'is_valid': {'required': False, 'allow_null': True},
            'status': {'required': False, 'allow_null': True},
        }


class HotelBookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer
    start_date = serializers.DateTimeField(format=None, input_formats=['%Y-%m-%d', ])
    end_date = serializers.DateTimeField(format=None, input_formats=['%Y-%m-%d', ])

    class Meta:
        model = HotelBooking
        fields = ['start_date', 'end_date', 'hotel', 'room']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['passenger'] = user
        return super(HotelBookingSerializer, self).create(validated_data)

    def validate(self, data):
        booked_times = HotelBooking.objects.filter(room=data['room'].id)
        for time in booked_times:
            if time.start_date <= data['start_date'] <= time.end_date or\
                    time.start_date <= data['end_date'] <= time.end_date:
                raise serializers.ValidationError({"room_status": "room is full at this time"})

        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"end_date": "finish must occur after start"})
        return data


class FlightTicketReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightTicketReservation
        fields = ['flight', 'passport_number']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['passenger'] = user

        return super(FlightTicketReserveSerializer, self).create(validated_data)

    def validate(self, data):
        flight_capacity = FlightTicket.objects.get(id=data['flight'].id).capacity
        if flight_capacity <= 0:
            raise serializers.ValidationError({'capacity_status': 'no more tickets available'})
        return data
