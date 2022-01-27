from django.urls import path

from . import views

urlpatterns = [
    path('detection/covid/', views.detectCovidInfectionProb),
    path('saveuser/', views.saveUser),
    path('login/', views.Login),
    path('getuserinfo/', views.getUserInfo),
]
