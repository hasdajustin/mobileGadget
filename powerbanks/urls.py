from django.urls import path
from . import views

urlpatterns = [
    path('', views.powerbanks, name='powerbanks'),
]