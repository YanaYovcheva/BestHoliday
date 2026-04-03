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

class CommentPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        comment = self.request.get_object()

        is_owner = user == comment.user
        is_support = user.groups.filter(name='Support').exists()

        return user.is_authrnticated and (is_owner or is_support)


class CommentEditView(LoginRequiredMixin, CommentPermissionMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'reviews/comment-edit.html'

    def get_success_url(self):
        return reverse_lazy('excursions:excursion-detail', kwargs={'slug': self.object.excursion.slug})


class CommentDeleteView(LoginRequiredMixin, CommentPermissionMixin, DeleteView):
    model = Comment
    template_name = 'reviews/comment-delete.html'

    def get_success_url(self):
        return reverse_lazy('excursions:excursion-detail', kwargs={'slug': self.object.excursion.slug})