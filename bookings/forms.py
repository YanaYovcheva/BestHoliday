from django import forms
from bookings.models import Booking


class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_people']
        labels = {
            'number_of_people': 'Number of people',
        }
        help_texts = {
            'number_of_people': 'Enter how many people will join the excursion'
        }
        error_messages = {
            'number_of_people': {
                'required': 'Please enter the number of people',
                'invalid': 'Please enter a valid number'
            }
        }
        widgets = {
            'number_of_people': forms.NumberInput(attrs={'min': 1}),
        }

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data['number_of_people']

        if number_of_people < 1:
            raise forms.ValidationError('You must enter a number greater than 0')

        return number_of_people

