"""
URL configuration for folioframe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from .views import *

urlpatterns = [
    path('', include("foliogate.urls")),
    path('admin/', admin.site.urls),
    path('home/', include("foliohome.urls")),
    re_path(r'^(?P<code>\d{3})/$', error, name='showErrorTemplate'),
]
if getattr(settings, "DEV_KEY", False):
    urlpatterns += [
        path('foliofin/', include("foliofin.urls")),
        path('bip/', include("bip.urls")),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)