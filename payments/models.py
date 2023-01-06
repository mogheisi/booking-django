from django.db import models
from users.models import User


class GuestUser(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    id_number = models.IntegerField(unique=True, primary_key=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total_price = models.IntegerField()
    total_discount = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ('S', 'Successful'),
        ('U', 'Unsuccessful'),
        ('P', 'Pending'),
        ('C', 'Canceled'),
    )
    payment_status = models.CharField(choices=status_choices, max_length=1)
    other_passengers = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    passengers_count = models.PositiveSmallIntegerField()

