from rest_framework import serializers
from residences.models import Hotel, Room, Address, Amenity, HotelComment, Policy, City, Country


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
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
    room_facilities = AmenitySerializer()

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
    facilities = AmenitySerializer()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description', 'rooms', 'rate',
                  'hotel_policies', 'facilities', 'address']

    def get_rooms(self, obj):
        rooms = Room.objects.filter(hotel=obj.id)
        return RoomSerializer(rooms, many=True).data
