from django.urls import path
from .import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name="home"),
    path('all_stocks/', views.all_stocks, name="all_stocks"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
