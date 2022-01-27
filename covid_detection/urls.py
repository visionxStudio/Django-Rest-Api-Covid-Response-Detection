from django.urls import path

from . import views

urlpatterns = [
    path('detection/covid/', views.detectCovidInfectionProb),
]
