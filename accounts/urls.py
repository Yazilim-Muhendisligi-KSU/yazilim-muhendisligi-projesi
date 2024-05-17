from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('get_watchlist/', views.get_watchlist, name='get_watchlist'),
    path('add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('get_drawing/', views.get_drawing, name='get_drawing'),
    path('add_drawing/', views.add_drawing, name='add_drawing'),
    path('remove_drawing/', views.remove_drawing, name='remove_drawing'),
]
