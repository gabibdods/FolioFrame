from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def panel(request):
    if not getattr(settings, 'DEV_KEY', False):
        return HttpResponse(status=305)
    return render(request, 'bip/panel.html', { "fastAPIHost": settings.FASTAPI_HOST, "fastAPIPort": settings.FASTAPI_PORT }, status=202)