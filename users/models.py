from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.PositiveBigIntegerField(unique=True, validators=[
        RegexValidator(r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.', 'invalid')
    ])

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['username']
