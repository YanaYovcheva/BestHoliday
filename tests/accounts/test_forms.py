from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from accounts.forms import AppUserCreationForm, UserEditForm, ProfileEditForm


UserModel = get_user_model()

class AppUserCreationFormTests(TestCase):
    def test_form_is_valid_with_correct_data(self):
        form = AppUserCreationForm(data={
            'username': 'test123',
            'email': 'test@example.com',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })

        self.assertTrue(form.is_valid())

    def test_form_is_valid_with_incorrect_data(self):
        form = AppUserCreationForm(data={
            'username': 'test123',
            'email': 'test@example.com',
            'password1': 'StrongPass123',
            'password2': 'DifferentPass123',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)


class UserEditFormTests(TestCase):
    def setUp(self):
        self.user = baker.make(UserModel)

    def test_email_filed_is_disabled(self):
        form = UserEditForm()

        self.assertTrue(form.fields['email'].disabled)


class ProfileEditFormTests(TestCase):
    def setUp(self):
        self.user = baker.make(UserModel)
        self.profile = self.user.profile

    def test_form_is_valid_with_correct_phone_number(self):
        form = ProfileEditForm(data={
            'phone_number': '+359123456789',
            'date_of_birth': '1970-01-01',
        })

        self.assertTrue(form.is_valid())

    def test_form_is_valid_with_incorrect_phone_number(self):
        form = ProfileEditForm(data={
            'phone_number': '123abc',
            'date_of_birth': '1970-01-01',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
