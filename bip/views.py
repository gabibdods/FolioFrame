from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def panel(request):
    #if request.headers.get('ElectronBypass') == settings.ELECTRON_BYPASS:
    return render(request, 'bip/panel.html', { "fastAPIURL": settings.FASTAPI_URL }, status=202)
    #return HttpResponse(status=305)
