from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import User, Analysis, WatchedStock,Notification

import json


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password')
        if not User.objects.filter(username=username, email=email).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'message': 'Registration successful'})
        else:
            return JsonResponse({'error': 'Username already exists'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            user = authenticate(request, email=email, password=password)


        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:

            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
      return JsonResponse({'error': 'Only POST requests allowed'}, status=405) 
  
def get_watchlist(request): # İzleme listesine çağırma işlemleri burada gerçekleştirilir
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=401)
    

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
        return JsonResponse({'error': 'Method not allowed'}, status=401)
    

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
        return JsonResponse({'error': 'Method not allowed'}, status=401)
    

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

def get_drawing(request): # İzleme listesine çağırma işlemleri burada gerçekleştirilir
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=401)
    

    user_id = request.POST.get("user_id")


    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)
    
    analysis = Analysis.objects.filter(user=user)

    return JsonResponse({'message': 'Drawing added'})


def add_drawing(request):     # Çizim ekleme işlemleri burada gerçekleştirilir analysis kısmı
 
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=401)
    

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
        return JsonResponse({'error': 'Method not allowed'}, status=401)
    

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


