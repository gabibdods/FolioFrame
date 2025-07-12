from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
import foliogate.views

class Block:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin') and (not request.user.is_staff):
            return redirect('/401')
        return self.get_response(request)

class Limit(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied) and getattr(request, 'limited', False):
            return redirect('/429')
        return None

class Authenticate:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method != 'GET':
            return self.get_response(request)
        else:
            if request.path.startswith('/428'):
                return render(request, 'error/428.html')
            if request.path.startswith('/gate'):
                return render(request, 'gate.html')
            if request.session.get('checked_js'):
                if request.COOKIES.get('js_enabled'):
                    if request.session.get('passed_captcha'):
                        return self.get_response(request)
                    else:
                        return redirect(reverse(foliogate.views.gate))
                else:
                    return redirect('/428')
            else:
                request.session['checked_js'] = True
                if request.COOKIES.get('js_enabled'):
                    return redirect(reverse(foliogate.views.gate))
                else:
                    return redirect(reverse(foliogate.views.gate))