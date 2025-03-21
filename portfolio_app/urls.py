from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #LandingPage
    path('contact/', views.contact_create, name='contact_create'), #ContactPage
]