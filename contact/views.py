from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm
from django.contrib import messages

def contact_page_view(request):
    if request.method == "POST":
        contact_method = ContactForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_method.name = name
        contact_method.email = email
        contact_method.phone = phone
        contact_method.message = message
        contact_method.save()
        messages.success(request, 'Thanks for getting in touch, ' + name + '. A member of the Modern Landscapes team will get back to you shortly.')
    return render(request, 'contact.html')