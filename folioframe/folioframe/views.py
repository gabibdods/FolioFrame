from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import HttpResponseNotFound

def showErrorTemplate(request, code):
    templateName = f"{code}.html"
    if code == '100' or code == '101' or code == '102' or code == '103' or code == '204' or code == '205' or code == '206' or code == '304':
        return render(request, templateName)
    try:
        return render(request, templateName, status=int(code))
    except TemplateDoesNotExist:
        return render(request, '404.html')