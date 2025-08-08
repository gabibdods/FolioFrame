from django.urls import path
from .views import *

urlpatterns = [
    path('', category, name='index'),
    path('<int:video_id>/', detail, name='detail'),
]