from django.urls import path
from . import views

urlpatterns = [
    path('', views.earphones, name='earphones'),
]