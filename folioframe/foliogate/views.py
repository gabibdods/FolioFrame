import requests
from django.conf import settings
from django.shortcuts import render, redirect
import foliohome.views as foliohome

def captcha_gate_view(request):
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
            return redirect('index')
        else:
            return redirect('/403')
    return render(request, 'gate.html')

def index(request):
    if not request.session.get('passed_captcha'):
        return redirect('captcha_gate')
    return redirect(foliohome.index)