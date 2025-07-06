from django.shortcuts import render, get_object_or_404
from .models import Video

def list(request):
    videos = Video.objects.all()
    return render(request, 'foliofin/catalogue.html', {'videos': videos})

def detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'foliofin/pannel.html', {'video': video})