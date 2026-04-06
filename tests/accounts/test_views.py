from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

UserModel = get_user_model()

class RegisterViewTests(TestCase):
    def test_register_creates_user(self):
        self.client.post(
            reverse('accounts:register'),
            data={
                'username': 'test123',
                'email': 'test@example.com',
                'password1': 'StrongPass123',
                'password2': 'StrongPass123',
            }
        )

        self.assertTrue(UserModel.objects.filter(username='test123').exists())

    def test_register_returns_200_and_uses_correct_template(self):
        response = self.client.get(reverse('accounts:register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register-page.html')


class ProfileDetailViewTests(TestCase):
    def setUp(self):
        self.user = baker.make(UserModel)
        self.user.set_password('StrongPass123')
        self.user.save()

    def test_profile_detail_requires_login(self):
        response = self.client.get(reverse('accounts:profile-detail'))

        self.assertEqual(response.status_code, 302)


class ProfileEditViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test123',
            email='test@example.com',
            password='StrongPass123',
        )

    def test_profile_edit_get_returns_200_for_authenticated_user(self):
        self.client.login(username='test123', password='StrongPass123')

        response = self.client.get(reverse('accounts:profile-edit'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile-edit-page.html')
