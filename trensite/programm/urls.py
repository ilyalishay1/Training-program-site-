from django.urls import path
from programm import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('offer/', views.offer, name='offer'),
]
