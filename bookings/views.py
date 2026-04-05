from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from bookings.forms import BookingCreateForm
from bookings.models import Booking, Favourite
from bookings.tasks import send_booking_confirmation_email
from excursions.models import Excursion


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingCreateForm
    template_name = 'bookings/booking-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.excursion = get_object_or_404(Excursion, slug=kwargs['slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.excursion = self.excursion
        response = super().form_valid(form)

        transaction.on_commit(lambda: send_booking_confirmation_email.delay(
            self.request.user.email,
            self.request.user.username,
            self.excursion.title,
        ))
        return response

    def get_success_url(self):
        return reverse_lazy('bookings:my-bookings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['excursion'] = self.excursion
        return context


class MyBookingsListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/my-bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        excursion = get_object_or_404(Excursion, slug=kwargs['slug'])
        Favourite.objects.get_or_create(
            user=request.user,
            excursion=excursion,
        )
        return redirect('excursions:excursion-detail', slug=excursion.slug)


class RemoveFromFavoritesView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        excursion = get_object_or_404(Excursion, slug=kwargs['slug'])
        favourite = Favourite.objects.filter(
            user=request.user,
            excursion=excursion,
        )
        favourite.delete()
        return redirect('excursions:excursion-detail', slug=excursion.slug)


class MyFavoritesListView(LoginRequiredMixin, ListView):
    model = Favourite
    template_name = 'bookings/my-favorites-page.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)
