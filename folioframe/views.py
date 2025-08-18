from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist

def error(request, code):
    template = f"error/{code}.html"
    if code == '100' or code == '101' or code == '102' or code == '103' or code == '204' or code == '205' or code == '206' or code == '304':
        return render(request, template)
    try:
        return render(request, template, status=int(code))
    except TemplateDoesNotExist:
        return redirect("/ff/416/")