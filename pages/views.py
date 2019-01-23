from django.shortcuts import render
from django.views.generic import TemplateView
from tours.models import Destination, Tour, TourDetail
from .forms import ContactUsForm
from django.core.mail import send_mail


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactUsForm
        return context

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid:
            send_mail(
                'Contact us inMyTours',
                'First Name: {}. \n Last name: {}. \n Email: {}. \n Message: {}'.format(
                    form.data['first_name'],
                    form.data['last_name'],
                    form.data['email'],
                    form.data['subject'],
                ),
                form.data['email'],
                ['slimaidarismail@gmail.com'],
                fail_silently=False,
            )
            context = super().get_context_data(**kwargs)
            context['form'] = ContactUsForm
            context['sent'] = True
            return self.render_to_response(context=context)
    

class PrivacytView(TemplateView):
    template_name = 'pages/privacy.html'
