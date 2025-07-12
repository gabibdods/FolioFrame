from django.shortcuts import render

def panel(request):
    return render(request, 'bip/panel.html')