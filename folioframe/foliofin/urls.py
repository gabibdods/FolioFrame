from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='index'),
    path('<int:video_id>/', views.detail, name='detail'),
]