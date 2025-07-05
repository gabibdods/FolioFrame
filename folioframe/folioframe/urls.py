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
from django.contrib import admin
from django.urls import include, path, re_path
import folioframe.views as folioframe

urlpatterns = [
    path('', include("foliogate.urls")),
    path('admin/', admin.site.urls),
    path('home/', include("foliohome.urls")),
    re_path(r'^(?P<code>\d{3})/$', folioframe.showErrorTemplate, name='showErrorTemplate'),
]