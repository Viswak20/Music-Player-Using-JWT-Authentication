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
        return JsonResponse({"Error":"Invalid Method"},staus=400)
    try:
        data = json.loads(request.body)
        email=data['email']
        password=data['password']
        response=authenticate_credentails(email,password)
        if response:
            request.session['jwt'] = response
            return JsonResponse({'message': request.session['jwt']},status=200)
        else:
            return JsonResponse({'error': 'Invalid credentails or user not found'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
def authenticate_credentails(email,password):
    try:
        user = User.objects.get(email=email)
        if user.password == password:
            payload = {
                    'user_id': user.id,
                    'email': user.email,
                    'exp': datetime.utcnow() + timedelta(minutes=60),
                    'iat': datetime.utcnow(),
                }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            
            return token
        else:
            return False
    except User.DoesNotExist:
        return False

def dashboard(request):

    token = request.session['jwt']
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
        if user:
            return render(request, "dashboard.html")
        return JsonResponse({'error': 'user does not exist'}, status=401)

    except jwt.ExpiredSignatureError:
        return HttpResponse(""" Token Expired. Redirecting to Login Page...
                            <script> setTimeout(function() { window.location.href = '/login/'; }, 2000); </script>
                        """)
    except jwt.InvalidTokenError:
        return HttpResponse("Invalid Token Redirecting to Login. <script> setTimeout(function() { window.location.href=('/login/') },5000); </script>")
    
def clearsession(request):
    request.session.flush()
    return redirect('login') 