from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from bookings.models import Booking, Favourite
from excursions.models import Destination, Excursion


UserModel = get_user_model()

class BookingViewsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test123',
            email='test@example.com',
            password='StrongPass123',
        )

        self.destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='Beautiful city',
        )

        self.excursion = Excursion.objects.create(
            title='Love Story in Paris',
            price=1200,
            start_date='2026-05-10',
            end_date='2026-05-15',
            image='excursions/test.jpg',
            description='Romantic getaway',
            category=Excursion.CategoryChoices.ROMANTIC,
            destination=self.destination,
        )

    def test_booking_create(self):
        self.client.login(username='test123', password='StrongPass123')

        response = self.client.post(
            reverse('bookings:create', kwargs={'slug': self.excursion.slug}),
            data={'number_of_people': 2},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(user=self.user, excursion=self.excursion).exists())

    def test_my_bookings_requires_login(self):
        response = self.client.get(reverse('bookings:my-bookings'))

        self.assertEqual(response.status_code, 302)

    def test_my_bookings_shows_only_logged_user_bookings(self):
        other_user = UserModel.objects.create_user(
            username='other123',
            email='other@example.com',
            password='StrongPass123',
        )

        user_booking = Booking.objects.create(
            user=self.user,
            excursion=self.excursion,
            number_of_people=2,
        )

        other_excursion = Excursion.objects.create(
            title='Summer in Rome',
            price=1500,
            start_date='2026-06-01',
            end_date='2026-06-07',
            image='excursions/test2.jpg',
            description='Great excursion',
            category=Excursion.CategoryChoices.CULTURAL,
            destination=self.destination,
        )

        other_booking = Booking.objects.create(
            user=other_user,
            excursion=other_excursion,
            number_of_people=3,
        )

        self.client.login(username='test123', password='StrongPass123')
        response = self.client.get(reverse('bookings:my-bookings'))

        self.assertIn(user_booking, response.context['bookings'])
        self.assertNotIn(other_booking, response.context['bookings'])


class FavouriteViewsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test123',
            email='test@example.com',
            password='StrongPass123',
        )

        self.destination = Destination.objects.create(
            name='Paris',
            country='France',
            description='Beautiful city',
        )

        self.excursion = Excursion.objects.create(
            title='Love Story in Paris',
            price=1200,
            start_date='2026-05-10',
            end_date='2026-05-15',
            image='excursions/test.jpg',
            description='Romantic getaway',
            category=Excursion.CategoryChoices.ROMANTIC,
            destination=self.destination,
        )

    def test_add_to_favorites_creates_favourite(self):
        self.client.login(username='test123', password='StrongPass123')

        self.client.post(reverse('bookings:add-favorite', kwargs={'slug': self.excursion.slug}))

        self.assertTrue(Favourite.objects.filter(user=self.user, excursion=self.excursion).exists())

    def test_remove_from_favorites_deletes_favourite(self):
        favourite = Favourite.objects.create(
            user=self.user,
            excursion=self.excursion,
        )

        self.client.login(username='test123', password='StrongPass123')

        self.client.post(reverse('bookings:remove-favorite', kwargs={'slug': self.excursion.slug}))

        self.assertFalse(Favourite.objects.filter(pk=favourite.pk).exists())
