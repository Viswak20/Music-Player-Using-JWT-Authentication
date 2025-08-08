from django.contrib import admin
from django.urls import path
from musicapp import views


urlpatterns = [
    path('login/', views.login,name='login'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('api/login/',views.authenticate_login,name='authenticate_login'),
] 