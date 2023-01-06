from django.core.cache import cache
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User
from utils.otp.otp import send_otp_to_user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_number')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', )
        extra_kwargs = {'phone_number': {'validators': []}}

    def create(self, validated_data):
        phone_number = validated_data['phone_number']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            random_username = f'user_{phone_number}'
            user = User.objects.create_user(random_username, phone_number=phone_number)

        send_otp_to_user(user)

        return user


class LoginStep2Serializer(serializers.ModelSerializer):
    otp_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'otp_code')
        extra_kwargs = {'phone_number': {'validators': [], 'write_only': True}}

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        otp = attrs['otp_code']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise ValidationError('Phone number does not exist')

        expected_otp = cache.get(f'otp_code:{user.phone_number}')
        if expected_otp != otp:
            raise ValidationError('The code you sent is invalid')

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        return user
