
from django.db import models
from django.conf import settings

class Car(models.Model):
    name = models.CharField(max_length=50)
    seats = models.PositiveIntegerField(default=4)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='booked')

    def __str__(self):
        return f"#{self.id} {self.user} -> {self.car}"
