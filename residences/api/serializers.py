from rest_framework import serializers
from residences.models import Hotel, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description', 'rooms', 'rate',
                  'hotel_policies', 'city', 'facilities', 'address']

    def get_rooms(self, obj):
        rooms = Room.objects.filter(hotel=obj.id)
        return RoomSerializer(rooms, many=True).data
