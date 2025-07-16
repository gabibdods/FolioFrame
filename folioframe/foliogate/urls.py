from django.urls import path
import foliogate.views as foliogate

urlpatterns = [
    path('', foliogate.index, name='index'),
    path('foliogate/', foliogate.gate, name='gate'),
]