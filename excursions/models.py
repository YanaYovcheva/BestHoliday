from django.db import models
from django.utils.text import slugify
from excursions.validators import validate_positive_price


class Destination(models.Model):
    name = models.CharField(
        max_length=50
    )
    country = models.CharField(
        max_length=50
    )
    description = models.TextField()
    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)


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
        validators=[validate_positive_price]
    )
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(
        upload_to='excursions/'
    )
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
    )
    slug = models.SlugField(
        unique=True,
        blank=True
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.start_date}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
