from django.db import models


class Destination(models.Model):
    name = models.CharField(
        max_length=50
    )
    country = models.CharField(
        max_length=50
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.country}"


class Feature(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Excursion(models.Model):
    class CategoryChoices(models.TextChoices):
        SEA = "Sea", "Sea"
        MOUNTAIN = "Mountain", "Mountain"
        CULTURAL = "Cultural", "Cultural"
        ADVENTURE = "Adventure", "Adventure"
        FAMILY = "Family", "Family"
        LUXURY = "Luxury", "Luxury"
        ROMANTIC = "Romantic", "Romantic"

    title = models.CharField(
        max_length=100
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(
        upload_to='excursions/'
    )
    description = models.TextField()
    available_seats = models.PositiveIntegerField()
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='excursions',
    )
    features = models.ManyToManyField(
        Feature,
        blank=True,
    )

    def __str__(self):
        return self.title
