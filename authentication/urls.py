from django.urls import path
from . import views

urlpatterns = [
    path('loginuser/', views.loginUser),
    path('registeruser/', views.registerUser),
    path('getuserinfo/', views.getUserInfo),
]
