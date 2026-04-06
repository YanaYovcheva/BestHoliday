from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker
from accounts.models import Profile
from accounts.validators import validate_phone_number


UserModel = get_user_model()

class ProfileModelTests(TestCase):
    def setUp(self):
        self.user = baker.make(UserModel)
        self.profile = self.user.profile

    def test_phone_number_validator_raises_for_invalid_number(self):
        with self.assertRaises(ValidationError) as error:
            validate_phone_number('123abc')

        self.assertEqual(error.exception.message, 'Phone number must contain between 10 and 15 digits and may start with +.')

    def test_profile_is_created_automatically(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())
