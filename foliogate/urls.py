from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('foliogate/', gate, name='gate'),
]