from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tour, TourDetail, Gallery

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
        return context
    
    

