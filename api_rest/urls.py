from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_manager, name='user_manager'), 
    path('user/<str:nick>/', views.user_manager, name='user_manager'), 
    ]   