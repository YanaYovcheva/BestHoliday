from django.contrib import admin
from bookings.models import Booking, Favourite


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'excursion', 'number_of_people', 'booked_on']


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'excursion']
