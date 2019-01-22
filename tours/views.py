from django.shortcuts import render
from django.views.generic import ListView
from .models import Tour, TourDetail

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
    
    

