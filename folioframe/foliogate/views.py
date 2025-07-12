from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django_ratelimit.decorators import ratelimit
import requests
import foliohome.views

@ratelimit(key='ip', rate='3/m', block=True)
def index(request):
    if not request.session.get('passed_captcha'):
        return redirect(reverse(gate))
    return redirect(reverse(foliohome.views.index))

@ratelimit(key='ip', rate='3/m', block=True)
def gate(request):
    if request.method == 'POST':
        token = request.POST.get('g-recaptcha-response')
        recaptcha_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': token
            }
        )
        result = recaptcha_response.json()
        if result.get('success') and result.get('score', 0) >= 0.5:
            request.session['passed_captcha'] = True
            return redirect(reverse(foliohome.views.index))
        else:
            return redirect('/403')
    return render(request, 'gate.html', status=428)

@ratelimit(key='ip', rate='3/m', block=False)
def block(request):
    if getattr(request, 'limited', False):
        return render(request, 'error/429.html', status=429)
    return None