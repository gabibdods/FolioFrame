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
        else:
            if request.path.startswith('/403'):
                return render(request, '403.html')
            if request.path.startswith('/gate'):
                return render(request, 'gate.html')
            if request.session.get('checked_js'):
                if request.COOKIES.get('js_enabled'):
                    if request.session.get('passed_captcha'):
                        return self.get_response(request)
                    else:
                        return redirect(reverse(foliogate.captcha_gate_view))
                else:
                    return redirect('/403')
            else:
                request.session['checked_js'] = True
                if request.COOKIES.get('js_enabled'):
                    return redirect(reverse(foliogate.captcha_gate_view))
                else:
                    return redirect(reverse(foliogate.captcha_gate_view))