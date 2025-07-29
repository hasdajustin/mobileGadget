from django.urls import path
from . import views

urlpatterns = [
    path('', views.cables, name='cables'),
]