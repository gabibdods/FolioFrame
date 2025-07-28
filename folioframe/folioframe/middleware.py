from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
import foliogate.views
from django.conf import settings

class Block:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin') and (not request.user.is_staff):
            return redirect('/401/')
        return self.get_response(request)

class Authenticate:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method != 'GET':
            return self.get_response(request)
        elif request.headers.get('ElectronBypass') == settings.ELECTRON_BYPASS:
            return self.get_response(request)
        else:
            if request.path.startswith('/428'):
                return render(request, 'error/428.html', status=428)
            if request.path.startswith('/foliogate'):
                return render(request, 'foliogate/gate.html', status=203)
            if request.session.get('checked_js'):
                if request.COOKIES.get('js_enabled'):
                    if request.session.get('passed_captcha'):
                        return self.get_response(request)
                    else:
                        return HttpResponse(status=205)
                else:
                    return redirect('/428/')
            else:
                request.session['checked_js'] = True
                if request.COOKIES.get('js_enabled'):
                    return HttpResponse(status=204)
                else:
                    return redirect(reverse(foliogate.views.gate))

class Limit(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied) and getattr(request, 'limited', False):
            return redirect('/429/')
        return None

class ErrorRedirect(MiddlewareMixin):
    def process_response(self, request, response):
        redirects = {
            305: '/305/', # /bip/
            400: '/400/', # client side error
            401: '/401/', # /admin/
            403: '/403/', # authentification fail
            404: '/404/', # unknown url
            407: '/407/', # /foliofin/
            412: '/412/', # honeypot
            416: '/416/', # r'/^(?P<code>\d{3})/$'
            428: '/428/', # js deactivated
            429: '/429/', # rate limited
            500: '/500/', # database misstep
            502: '/502/', # cloudflare fail
        }
        if request.path in redirects.values():
            return response
        if response.status_code in redirects:
            return redirect(redirects[response.status_code])
        return response