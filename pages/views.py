from django.shortcuts import render
from django.views.generic import TemplateView
from tours.models import Destination, Tour, TourDetail

class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destinations"] = Destination.objects.all()
        context["tours"] = TourDetail.objects.filter(tour__feautured=True)
        return context
    
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class PrivacytView(TemplateView):
    template_name = 'pages/privacy.html'
