from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from excursions.models import Destination, Excursion


UserModel = get_user_model()

class ExcursionViewsTests(TestCase):
    def setUp(self):
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

    def test_excursion_list_view_returns_200(self):
        response = self.client.get(reverse('excursions:excursion-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excursions/excursion-list.html')


    def test_logged_user_can_open_excursion_list_view(self):
        self.client.login(username='test123', password='StrongPass123')

        response = self.client.get(reverse('excursions:excursion-list'))

        self.assertEqual(response.status_code, 200)

    def test_excursion_detail_view_returns_200(self):
        response = self.client.get(
            reverse('excursions:excursion-detail', kwargs={'slug': self.excursion.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excursions/excursion-detail.html')

