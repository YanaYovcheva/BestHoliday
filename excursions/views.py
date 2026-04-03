from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from excursions.forms import ExcursionCreateEditForm, DestinationCreateEditForm, FeatureCreateEditForm
from excursions.models import Excursion, Destination, Feature


class ExcursionListView(ListView):
    model = Excursion
    template_name = 'excursions/excursion-list.html'
    context_object_name = 'excursions'


class ExcursionDetailView(DetailView):
    model = Excursion
    template_name = 'excursions/excursion-detail.html'
    context_object_name = 'excursion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['is_favorite'] = self.object.favorites.filter(
                user=self.request.user
            ).exists()
            context['is_support'] = self.request.user.groups.filter(
                name='Support'
            ).exists()
        else:
            context['is_favorite'] = False
            context['is_support'] = False

        return context


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_authenticated
                and
            self.request.user.groups.filter(name='Mangers').exists()
        )


class ExcursionCreateView(StaffRequiredMixin, CreateView):
    model = Excursion
    form_class = ExcursionCreateEditForm
    template_name = 'excursions/excursion-create.html'
    success_url = reverse_lazy('excursions:excursion-list')


class ExcursionEditView(StaffRequiredMixin, UpdateView):
    model = Excursion
    form_class = ExcursionCreateEditForm
    template_name = 'excursions/excursion-edit.html'

    def get_success_url(self):
        return reverse_lazy('excursions:excursion-detail', kwargs={'slug': self.object.slug})


class ExcursionDeleteView(StaffRequiredMixin, DeleteView):
    model = Excursion
    template_name = 'excursions/excursion-delete.html'
    success_url = reverse_lazy('excursions:excursion-list')


# TODO make the destination views REST
class DestinationListView(ListView):
    model = Destination
    template_name = 'excursions/destination-list.html'
    context_object_name = 'destinations'


class DestinationCreateView(StaffRequiredMixin, CreateView):
    model = Destination
    form_class = DestinationCreateEditForm
    template_name = 'excursions/destination-create.html'
    success_url = reverse_lazy('excursions:destination-list')


class DestinationEditView(StaffRequiredMixin, UpdateView):
    model = Destination
    form_class = DestinationCreateEditForm
    template_name = 'excursions/destination-edit.html'
    success_url = reverse_lazy('excursions:destination-list')


class DestinationDeleteView(StaffRequiredMixin, DeleteView):
    model = Destination
    template_name = 'excursions/destination-delete.html'
    success_url = reverse_lazy('excursions:destination-list')


class FeatureListView(ListView):
    model = Feature
    template_name = 'excursions/feature-list.html'
    context_object_name = 'features'


class FeatureCreateView(StaffRequiredMixin, CreateView):
    model = Feature
    form_class = FeatureCreateEditForm
    template_name = 'excursions/feature-create.html'
    success_url = reverse_lazy('excursions:feature-list')


class FeatureEditView(StaffRequiredMixin, UpdateView):
    model = Feature
    form_class = FeatureCreateEditForm
    template_name = 'excursions/feature-edit.html'
    success_url = reverse_lazy('excursions:feature-list')


class FeatureDeleteView(StaffRequiredMixin, DeleteView):
    model = Feature
    template_name = 'excursions/feature-delete.html'
    success_url = reverse_lazy('excursions:feature-list')