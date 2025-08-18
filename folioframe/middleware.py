from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.conf import settings
import foliogate.views

class Block:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/ff/admin') and (not request.user.is_staff):
            return redirect('/ff/401/')
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
            if request.path.startswith('/ff/428'):
                return render(request, 'error/428.html', status=428)
            if request.path.startswith('/ff/gate'):
                return render(request, 'foliogate/gate.html', status=203)
            if request.session.get('checked_js'):
                if request.COOKIES.get('js_enabled'):
                    return self.get_response(request)
                else:
                    return redirect('/ff/428/')
            else:
                request.session['checked_js'] = True
                if request.COOKIES.get('js_enabled'):
                    return HttpResponse(status=204)
                else:
                    return redirect(reverse(foliogate.views.index))

class Limit(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied) and getattr(request, 'limited', False):
            return redirect('/ff/429/')
        return None

class ErrorRedirect(MiddlewareMixin):
    def process_response(self, request, response):
        redirects = {
            305: '/ff/305/', # /bip/
            400: '/ff/400/', # client side error
            401: '/ff/401/', # /admin/
            403: '/ff/403/', # captcha fail
            404: '/ff/404/', # unknown url
            407: '/ff/407/', # /foliofin/
            410: '/ff/410/', # REST get fail
            412: '/ff/412/', # honeypot
            416: '/ff/416/', # r'/^(?P<code>\d{3})/$'
            417: '/ff/417/', # /foliofin/<int:video_id>/
            423: '/ff/423/', # REST authentication fail
            428: '/ff/428/', # js deactivated
            429: '/ff/429/', # rate limit
            500: '/ff/500/', # database migration needed
            502: '/ff/502/', # cloudflared fail
            511: '/ff/511/', # REST authentication expired
        }
        if request.path in redirects.values():
            return response
        if response.status_code in redirects:
            return redirect(redirects[response.status_code])
        return response
