from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from excursions.models import Excursion
from reviews.forms import CommentForm
from reviews.models import Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'reviews/comment-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.excursion = get_object_or_404(Excursion, slug=kwargs['slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.excursion = self.excursion
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('excursions:excursion-detail', kwargs={'slug': self.excursion.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['excursion'] = self.excursion
        return context

class CommentOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().user


class CommentEditView(LoginRequiredMixin, CommentOwnerMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'reviews/comment-edit.html'

    def get_success_url(self):
        return reverse_lazy('excursions:excursion-detail', kwargs={'slug': self.object.excursion.slug})


class CommentDeleteView(LoginRequiredMixin, CommentOwnerMixin, DeleteView):
    model = Comment
    template_name = 'reviews/comment-delete.html'

    def get_success_url(self):
        return reverse_lazy('excursions:excursion-detail', kwargs={'slug': self.object.excursion.slug})