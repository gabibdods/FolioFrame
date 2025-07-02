from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    if request.POST.get('surprise'):
        return render(request, '403.html')
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            subject = f"Subject: {subject}"
            message_body = f"New Contact From Web Site Form Submission: {name} at <{email}>\n\n{message}"
            from_email = 'gabriel.ods.14@hotmail.com'
            to_email = ['gabriel.ods.14@hotmail.com']
            send_mail(subject, message_body, from_email, to_email)
            return redirect('success')
    else:
        form = ContactForm()
    return redirect('/')