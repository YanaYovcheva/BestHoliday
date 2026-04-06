from datetime import date, timedelta
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker
from excursions.models import Destination, Excursion


class ExcursionModelTests(TestCase):
    def setUp(self):
        self.destination = baker.make(
            Destination,
            name='Paris',
            country='France',
            description='Beautiful city',
        )

    def test_excursion_raises_error_when_price_is_negative(self):
        excursion = Excursion(
            title='Love Story in Paris',
            destination=self.destination,
            price=Decimal('-1.00'),
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5),
            image='excursions/test.jpg',
            description='Romantic getaway',
            category=Excursion.CategoryChoices.ROMANTIC,
        )

        with self.assertRaises(ValidationError) as error:
            excursion.full_clean()

        self.assertIn('price', error.exception.message_dict)
        self.assertEqual(error.exception.message_dict['price'][0], 'Price must be greater than 0.')

    def test_excursion_str_returns_title(self):
        excursion = Excursion(
            title='Love Story in Paris',
            price=Decimal('1200.00'),
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5),
            image='excursions/test.jpg',
            description='Romantic getaway',
            category=Excursion.CategoryChoices.ROMANTIC,
            destination=self.destination,
        )

        self.assertEqual(str(excursion), 'Love Story in Paris')


class DestinationModelTests(TestCase):
    def test_destination_str_returns_name_and_country(self):
        destination = Destination(
            name='Paris',
            country='France',
            description='Beautiful city',
        )

        self.assertEqual(str(destination), 'Paris, France')

    def test_destination_slug_is_generated_on_save(self):
        destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='Beautiful city',
        )

        self.assertEqual(destination.slug, 'paris-france')