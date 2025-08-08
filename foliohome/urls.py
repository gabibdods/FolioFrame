from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('api/download/resume/', ResumeDownloadViewSet.as_view(), name='resume-download'),
]