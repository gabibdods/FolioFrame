from django.urls import path
import foliohome.views

urlpatterns = [
    path('', foliohome.views.index, name="index"),
    path('contact/', foliohome.views.contact, name='contact'),
    path('success/', foliohome.views.success, name='success'),
]