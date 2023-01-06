from rest_framework import serializers
from datetime import datetime

from reservations.models import HotelBooking
from residences.models import Hotel, Room, Address, Facility, HotelComment, Policy, City, Country


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    room_facilities = FacilitySerializer()

    class Meta:
        model = Room
        fields = "__all__"


class HotelCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelComment
        fields = "__all__"


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()
    address = AddressSerializer()
    comments = HotelComment()
    hotel_policies = PolicySerializer()
    facilities = FacilitySerializer()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description', 'rooms', 'rate',
                  'hotel_policies', 'facilities', 'address']

    def get_rooms(self, obj):
        rooms = Room.objects.filter(hotel=obj.id)
        return RoomSerializer(rooms, many=True).data
