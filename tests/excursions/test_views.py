from django.contrib.auth import get_user_model
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

        self.second_destination = Destination.objects.create(
            name='Rome',
            country='Italy',
            description='Beautiful city',
        )

        self.second_excursion = Excursion.objects.create(
            title='Summer in Rome',
            price=1500,
            start_date='2026-06-01',
            end_date='2026-06-07',
            image='excursions/test2.jpg',
            description='Amazing summer excursion',
            category=Excursion.CategoryChoices.CULTURAL,
            destination=self.second_destination,
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


    def test_excursion_search_bar_results_by_title(self):
        response = self.client.get(reverse('excursions:excursion-list'), {'query':'Paris'})

        self.assertContains(response, self.excursion.title)
        self.assertNotContains(response, self.second_excursion.title)

    def test_excursion_search_bar_results_by_country(self):
        response = self.client.get(reverse('excursions:excursion-list'), {'query':'France'})

        self.assertContains(response, self.destination.name)
        self.assertNotContains(response, self.second_destination.name)
