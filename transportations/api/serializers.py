from rest_framework import serializers
from transportations.models import FlightTicket, FlightTypePrice, Airport, Airline
from residences.models import Facility, City, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(serializers.ModelSerializer)

    class Meta:
        model = City
        fields = ['city_name', 'country']


class AirportSerializer(serializers.ModelSerializer):

    city = CitySerializer()

    class Meta:
        model = Airport
        fields = ['city', 'airport_name']


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['title']


class FlightPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightTypePrice
        fields = ['flight_type', 'price']


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    facilities = FacilitySerializer()
    origin_airport = AirportSerializer()
    destination_airport = AirportSerializer()
    origin = CitySerializer()
    destination = CitySerializer()

    def create(self, validated_data):
        amenities = Facility.objects.create(validated_data.pop('amenities'))
        airline = Airline.objects.create(validated_data.pop('airline'))
        origin_airport = Airport.objects.create(validated_data.pop('origin_airport'))
        destination_airport = Airport.objects.create(validated_data.pop('destination_airport'))
        origin = City.objects.create(validated_data.pop('origin'))
        destination = City.objects.create(validated_data.pop('destination'))
        instance = FlightTicket.objects.create(**validated_data)
        return instance

    class Meta:
        model = FlightTicket
        fields = ('origin', 'origin_airport', 'destination', 'destination_airport',
                  'departure_time', 'arrival_time', 'airline', 'price', 'capacity',
                  'flight_number', 'facilities',
                  )
