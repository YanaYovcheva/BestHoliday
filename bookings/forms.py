from django import forms
from bookings.models import Booking


class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_people']
        labels = {
            'number_of_people': 'Number of people',
        }
        widgets = {
            'number_of_people': forms.NumberInput(attrs={'min': 1}),
        }
