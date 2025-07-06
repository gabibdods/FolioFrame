from django.urls import path
from django.views.generic import TemplateView
import foliohome.views as foliohome

urlpatterns = [
    path('', foliohome.index, name="index"),
    path('contact/', foliohome.contact, name='contact'),
    path('success/', foliohome.success, name='success'),
]