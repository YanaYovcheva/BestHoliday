from django.contrib import admin
from excursions.models import Excursion, Destination, Feature


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name', 'country']
    
    
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'destination', 'category', 'start_date', 'end_date']
    list_filter = ['category', 'destination', 'start_date']
    search_fields = ['title', 'destination__name', 'destination__country']
