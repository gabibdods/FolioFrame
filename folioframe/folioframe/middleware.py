from django.shortcuts import render, redirect
import foliogate.views as foliogate
from django.urls import reverse

def blockAdmin(get_response):
    def middleware(request):
        if request.path.startswith('/admin') and (not request.user.is_staff):
            return redirect('/403')
        return get_response(request)
    return middleware

class JavaScriptCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method != 'GET':
            return self.get_response(request)
        jsEnabled = request.COOKIES.get('js_enabled')
        if jsEnabled:
            return self.get_response(request)
        if not request.session.get('checked_js'):
            request.session['checked_js'] = True
            return redirect(reverse(foliogate.captcha_gate_view))
        if not request.path.startswith('/gate/'):
            return redirect('/403')
        return self.get_response(request)