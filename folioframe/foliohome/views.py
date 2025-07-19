from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactForm
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/h', block=True)
def index(request):
    if request.POST.get('surprise'):
        return HttpResponse(status=412)
    return render(request, 'foliohome/index.html', status=202)

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