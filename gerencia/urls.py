from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerencia_index, name='gerencia_index'),
]