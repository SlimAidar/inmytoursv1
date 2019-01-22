from django.urls import path, include
from . import views


urlpatterns = [
    path('tours/', views.TourListView.as_view(), name="tour_list"),
]