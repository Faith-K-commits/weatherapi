from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.temperature, name='temp'),
]