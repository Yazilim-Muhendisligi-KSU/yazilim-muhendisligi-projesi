from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import User


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
    


