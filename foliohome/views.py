from django.core.mail import send_mail
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import signing
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from pathlib import Path
from django.conf import settings
from .forms import ContactForm
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/h', block=True)
def index(request):
    if request.POST.get('surprise'):
        return HttpResponse(status=412)
    token = signing.dumps({"resume": True})
    return render(request, 'foliohome/index.html', { "download_token": token }, status=202)

@ratelimit(key='ip', rate='10/h', block=True)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            subject = f"Subject: {subject}"
            message_body = f"New Contact From Web Site Form Submission : {name} at <{email}>\n\n{message}"
            from_email = 'gabriel.ods.14@hotmail.com'
            to_email = ['gabriel.ods.14@hotmail.com']
            send_mail(subject, message_body, from_email, to_email)
            return redirect(reverse(success))
    return redirect(reverse(index))

@ratelimit(key='ip', rate='10/h', block=True)
def success(request):
    return render(request, 'foliohome/success.html', status=201)

@ratelimit(key='ip', rate='10/h', block=False)
def block(request):
    if getattr(request, 'limited', False):
        return HttpResponse(status=429)
    return None

class ResumeDownloadViewSet(APIView):
    permission_classes = [AllowAny]

    def get(self, request) -> HttpResponse | FileResponse:
        token = request.GET.get('token')
        try:
            signing.loads(token, max_age=300)
        except signing.SignatureExpired:
            return HttpResponse(status=511)
        except signing.BadSignature:
            return HttpResponse("Invalid download link.", status=423)

        file_path = Path(settings.MEDIA_ROOT) / "CurriculumVitae.pdf"
        if not file_path.exists():
            return HttpResponse(status=410)
        response = FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename='CurriculumVitae.pdf',
            content_type='application/pdf'
        )
        response["Cache-Control"] = "private, no-cache, no-store, must-revalidate, max-age=0"
        response["Pragma"] = "no-cache"
        response["Expires"] = "0"
        response["X-Content-Type-Options"] = "nosniff"
        return response