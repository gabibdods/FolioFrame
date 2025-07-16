from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='index'),
    path('<int:video_id>/', views.detail, name='detail'),
]