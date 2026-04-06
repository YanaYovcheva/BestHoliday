from django.core.exceptions import ValidationError


def validate_positive_price(value):
    if value <= 0:
        raise ValidationError('Price must be greater than 0.')


def validate_start_end_dates(start_date, end_date):
    if end_date < start_date:
        raise ValidationError('End date cannot be earlier than start date.')
