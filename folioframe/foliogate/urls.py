from django.urls import path
import foliogate.views as foliogate

urlpatterns = [
    path('', foliogate.index, name='index'),
    path('gate/', foliogate.captcha_gate_view, name='captcha_gate'),
]