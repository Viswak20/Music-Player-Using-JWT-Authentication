from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import json
import jwt
from django.views.decorators.csrf import csrf_exempt
from .models import*
from datetime import datetime, timedelta
from django.conf import settings
import time

# Create your views here.

def login(request):
    return render(request,"login.html")

@csrf_exempt 
def authenticate_login(request):
    if request.method !='POST':
        return JsonResponse({"Error":"Inavalid Method"},staus=400)
    try:
        data = json.loads(request.body)
        email=data['email']
        password=data['password']
        response=authenticate_credentails(email,password)
        response = authenticate_credentails(email, password)

        if response:
            res = JsonResponse({'message': 'Login successful'}, status=200)
            res.set_cookie(
                key='jwt',
                value=response,
                httponly=True,
                secure=True,   
                samesite='Lax',
                max_age=60
            )
            return res
        else:
            return JsonResponse({'Error': 'Invalid credentails or user not found'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
def authenticate_credentails(email,password):
    try:
        user = User.objects.get(email=email)
        if user.password == password:
            payload = {
                    'user_id': user.id,
                    'email': user.email,
                    'exp': datetime.utcnow() + timedelta(minutes=1),
                    'iat': datetime.utcnow(),
                }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return token
        else:
            return False
    except User.DoesNotExist:
        return False

def dashboard(request):
    return render(request, "dashboard.html")
