from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video

def category(request):
    if not getattr(settings, 'DEV_KEY', False):
        return HttpResponse(status=407)
    videos = Video.objects.all()
    return render(request, 'foliofin/catalogue.html', {'videos': videos}, status=202)

def detail(request, video_id):
    if not getattr(settings, 'DEV_KEY', False):
        return HttpResponse(status=417)
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'foliofin/panel.html', {'video': video}, status=201)