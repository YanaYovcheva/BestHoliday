from django import forms
from excursions.models import Excursion, Destination, Feature


class ExcursionCreateEditForm(forms.ModelForm):
    class Meta:
        model = Excursion
        exclude = ['available_seats']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter excursion title'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
        }


class DestinationCreateEditForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter destination name'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
        }


class FeatureCreateEditForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter feature name'}),
        }
