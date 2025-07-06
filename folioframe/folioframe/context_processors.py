from django.conf import settings


def version(request):
    return {'app_version': settings.APP_VERSION}