from rest_framework import serializers

from reservations.models import HotelBooking
from residences.models import Room


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

    class Meta:
        model = HotelBooking
        fields = ['start_date', 'end_date', 'hotel', 'room', 'passenger']

    def validate(self, data):
        room_status = Room.objects.get(id=data['room'].id).status
        if room_status == '1':
            raise serializers.ValidationError({"room_status": "room is full"})
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"end_date": "finish must occur after start"})
        return data
