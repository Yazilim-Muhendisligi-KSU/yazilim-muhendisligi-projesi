from django.urls import path
from .import views


urlpatterns = [
    path("Stocks",views.stocks),

]
