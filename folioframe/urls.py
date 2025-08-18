from django.contrib import admin
from django.urls import include, path, re_path
from .views import *

def root(_): return redirect('/ff/gate/')

urlpatterns = [
    path('', root, name='root'),
    path('gate/', include("foliogate.urls")),
    path('admin/', admin.site.urls),
    path('home/', include("foliohome.urls")),
    re_path(r'^(?P<code>\d{3})/$', error, name='showErrorTemplate'),
    path('fin/', include("foliofin.urls")),
    path('bip/', include("bip.urls")),
]
