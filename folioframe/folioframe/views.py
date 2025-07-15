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

def error400(request, exception):
    return render(request, 'error/400.html', status=400)

def error403(request, exception):
    return render(request, 'error/403.html', status=403)

def error404(request, exception):
    return render(request, 'error/404.html', status=404)

def error500(request):
    return render(request, 'error/500.html', status=500)