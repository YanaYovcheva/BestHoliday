from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.validators import validate_phone_number


class BestHolidayUser(AbstractUser):
    email = models.EmailField(
        unique=True,
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        BestHolidayUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )
    phone_number = models.CharField(
        max_length=16,
        validators=[validate_phone_number],
        blank=True,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
