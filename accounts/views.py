from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm, LoginForm
from .models import User, Analysis, WatchedStock, Notification

import json

### AUTH VIEWS START ###
# myapp/views.py


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:home')
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:home')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')
### AUTH VIEWS END ###


### WATCHLIST VIEWS START ###
def get_watchlist(request): # İzleme listesine çağırma işlemleri burada gerçekleştirilir
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    user_id = request.POST.get("user_id")

    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    
    watched_stocks = WatchedStock.objects.filter(user=user)

    data = {
        "watched_stocks": {
            watched_stock.stock_symbol
        for watched_stock in watched_stocks }
    }

    return JsonResponse(data)


def add_to_watchlist(request): # İzleme listesine ekleme işlemleri burada gerçekleştirilir
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

    user_id = request.POST.get("user_id")
    stock_symbol = request.POST.get("stock_symbol")


    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    

    watched_stock = WatchedStock.objects.create(user=user, stock_symbol=stock_symbol)

    return JsonResponse({'message': 'Added to watchlist'})


def remove_from_watchlist(request):     # İzleme listesinden çıkarma işlemleri burada gerçekleştirilir

    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

    user_id = request.POST.get("user_id")
    stock_symbol = request.POST.get("stock_symbol")


    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    
    try:
        watched_stock = WatchedStock.objects.get(user=user, stock_symbol=stock_symbol)
    except WatchedStock.DoesNotExist:
        return JsonResponse({'error': 'Watched stock does not exist'}, status=400)

    watched_stock.delete()
    
    return JsonResponse({'message': 'Removed from watchlist'})
### WATCHLIST VIEWS END ###


### DRAWING VIEWS START ###
def get_drawing(request): # İzleme listesine çağırma işlemleri burada gerçekleştirilir
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

    user_id = request.POST.get("user_id")


    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    
    analysis = Analysis.objects.filter(user=user)

    return JsonResponse({'message': 'Drawing added'})


def add_drawing(request):     # Çizim ekleme işlemleri burada gerçekleştirilir analysis kısmı
 
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

    user_id = request.POST.get("user_id")
    stock_symbol = request.POST.get("stock_symbol")
    data=request.POST.get("data")


    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    
    try:
        analysis = Analysis.objects.get(stock_symbol=stock_symbol,data=data,user=user)
    except Analysis.DoesNotExist:
        return JsonResponse({'error': 'Analysis does not exist'}, status=400)

    return JsonResponse({'message': 'Drawing added'})


def remove_drawing(request):     # Çizim silme işlemleri burada gerçekleştirilir
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

    user_id = request.POST.get("user_id")
    stock_symbol = request.POST.get("stock_symbol")
    data=request.POST.get("data")


    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    
    try:
        analysis = Analysis.objects.get(stock_symbol=stock_symbol,data=data,user=user)
    except Analysis.DoesNotExist:
        return JsonResponse({'error': 'Analysis does not exist'}, status=400)
     
    analysis.delete()

    return JsonResponse({'message': 'Drawing removed'})
### DRAWING VIEWS END ###


