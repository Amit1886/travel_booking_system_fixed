
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('driver', 'Driver'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=15, blank=True, null=True)
    kyc_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"
