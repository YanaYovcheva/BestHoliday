from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation_email(user_email, username, excursion_title):
    send_mail(
        subject='Booking Confirmation - BestHoliday',
        message=(f'Hello {username}\n'
                f'Your booking for "{excursion_title}" was created successfully.\n'
                f'Thank you for choosing BestHoliday!'),
        recipient_list=[user_email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        fail_silently=False,
    )
