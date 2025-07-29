from django.urls import path
from . import views

urlpatterns = [
    path('', views.chargers, name='chargers'),
]