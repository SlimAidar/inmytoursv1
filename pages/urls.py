from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('about', views.AboutView.as_view(), name="about_page"),
    path('contact', views.ContactView.as_view(), name="contact_page"),
    path('privacy', views.PrivacytView.as_view(), name="privacy_page"),
]