from rest_framework import serializers
from excursions.models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'description']
