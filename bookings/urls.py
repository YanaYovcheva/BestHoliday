from django.urls import path
from bookings import views


app_name = 'bookings'

urlpatterns = [
    path('my-bookings/', views.MyBookingsListView.as_view(), name='my-bookings'),
    path('favorites/', views.MyFavoritesListView.as_view(), name='my-favorites'),
    path('favorites/add/<slug:slug>/', views.AddToFavoritesView.as_view(), name='add-favorite'),
    path('favorites/remove/<slug:slug>/', views.RemoveFromFavoritesView.as_view(), name='remove-favorite'),
    path('create/<slug:slug>/', views.BookingCreateView.as_view(), name='create'),
]