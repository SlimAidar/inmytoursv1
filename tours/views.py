from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tour, TourDetail, Gallery, Book
from .forms import BookForm
from django.core.mail import send_mail
from django.conf import settings


class TourListView(ListView):
    model = TourDetail
    template_name = "tours/tour_list.html"
    paginate_by = 12

    def get_queryset(self):
        destination = self.request.GET.get('destination') or None
        if destination is not None:
            return TourDetail.objects.filter(tour__destination__name=destination)
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["destination"] = self.request.GET.get('destination')
        return context
    
    
class TourDetailView(DetailView):
    model = TourDetail
    template_name = "tours/tour_detail.html"
    context_object_name = "tour"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_detail = self.get_object()
        context["gallery"] = Gallery.objects.filter(tour__id=tour_detail.tour.id)
        context['form'] = BookForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid:
            tour_detail = self.get_object()
            booking = Book(
                tour = tour_detail.tour,
                first_name = form.data['first_name'],
                last_name = form.data['last_name'],
                email = form.data['email'],
                phone = form.data['phone'],
                message = form.data['message'],
            )
            booking.save()
            send_mail(
                'New booking inMyTours',
                'First Name: {}. \n Last name: {}. \n Phone: {}. \n Message: {}'.format(
                    booking.first_name,
                    booking.last_name,
                    booking.phone,
                    booking.message,
                ),
                booking.email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = BookForm
            context['sent'] = True
            return self.render_to_response(context=context)

    

