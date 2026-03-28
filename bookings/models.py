from django.conf import settings
from django.db import models
from excursions.models import Excursion


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    excursion = models.ForeignKey(
        Excursion,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    number_of_people = models.PositiveIntegerField()
    booked_on = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.user} - {self.excursion}'


class Favourite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    excursion = models.ForeignKey(
        Excursion,
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:
        ordering = ['excursion__title']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'excursion'],
                name='unique_user_excursion',
            )
        ]


    def __str__(self):
        return f"{self.user}'s favourite - {self.excursion}"
