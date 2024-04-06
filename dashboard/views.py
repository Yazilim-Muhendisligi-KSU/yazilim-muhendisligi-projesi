from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("dashboard")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")


