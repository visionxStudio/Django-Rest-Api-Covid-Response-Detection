from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login),
    path('saveuser/', views.saveUser),
    path('getuserinfo/', views.getUserInfo),
]
