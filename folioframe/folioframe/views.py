from django.conf import settings
from django.shortcuts import render
from django.template import TemplateDoesNotExist

def error(request, code):
    template = f"error/{code}.html"
    if code == '100' or code == '101' or code == '102' or code == '103' or code == '204' or code == '205' or code == '206' or code == '304':
        return render(request, template)
    try:
        return render(request, template, status=int(code))
    except TemplateDoesNotExist:
        return render(request, 'error/416.html', status=416)