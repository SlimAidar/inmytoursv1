from django.urls import path, include
from . import views


urlpatterns = [
    path('tours/<str:slug>', views.TourDetailView.as_view(), name="tour_detail"),
    path('tours/', views.TourListView.as_view(), name="tour_list"),
]