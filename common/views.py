from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'common/home.html'

class AboutPageView(TemplateView):
    template_name = 'common/about-page.html'


class ContactPageView(TemplateView):
    template_name = 'common/contact-page.html'

