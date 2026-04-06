from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from excursions.models import Destination, Excursion
from reviews.models import Comment


UserModel = get_user_model()

class CommentViewsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test123',
            email='test@example.com',
            password='StrongPass123',
        )

        self.owner = UserModel.objects.create_user(
            username='owner123',
            email='owner@example.com',
            password='StrongPass123',
        )

        self.other_user = UserModel.objects.create_user(
            username='other123',
            email='other@example.com',
            password='StrongPass123',
        )

        self.support_group, _ = Group.objects.get_or_create(name='Support')
        self.support_user = UserModel.objects.create_user(
            username='support123',
            email='support@example.com',
            password='StrongPass123',
        )
        self.support_user.groups.add(self.support_group)

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

        self.comment = Comment.objects.create(
            user=self.owner,
            excursion=self.excursion,
            content='Amazing excursion!',
        )

    def test_comment_owner_can_open_edit_page(self):
        self.client.login(username='owner123', password='StrongPass123')

        response = self.client.get(
            reverse('reviews:edit', kwargs={'pk': self.comment.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_non_owner_cannot_open_edit_page(self):
        self.client.login(username='other123', password='StrongPass123')

        response = self.client.get(
            reverse('reviews:edit', kwargs={'pk': self.comment.pk})
        )

        self.assertEqual(response.status_code, 403)

    def test_support_user_can_open_edit_page_for_any_comment(self):
        self.client.login(username='support123', password='StrongPass123')

        response = self.client.get(
            reverse('reviews:edit', kwargs={'pk': self.comment.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_comment_owner_can_delete_comment(self):
        self.client.login(username='owner123', password='StrongPass123')

        response = self.client.post(
            reverse('reviews:delete', kwargs={'pk': self.comment.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())
