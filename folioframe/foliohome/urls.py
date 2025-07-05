from django.urls import path
from django.views.generic import TemplateView
import foliohome.views as foliohome

urlpatterns = [
    path('', foliohome.index, name="index"),
    path('contact/', foliohome.contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]