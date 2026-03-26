import re
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not re.match(r'^\+?\d{10,15}$', value):
        raise ValidationError(
            'Phone number must contain between 10 and 15 digits and may start with +.'
        )