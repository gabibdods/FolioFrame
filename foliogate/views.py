from django.http import HttpResponse
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='3/m', block=True)
def index(request):
    return render(request, 'foliogate/gate.html', status=202)

@ratelimit(key='ip', rate='3/m', block=False)
def block(request):
    if getattr(request, 'limited', False):
        return HttpResponse(status=429)
    return None
