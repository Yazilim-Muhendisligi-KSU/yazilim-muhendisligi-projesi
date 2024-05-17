from django.urls import path
from .import views


urlpatterns = [
    path('', views.index),
    path('all_stocks/', views.all_stocks),
    path('about/', views.about),
    path('contact/', views.contact),


    
]
