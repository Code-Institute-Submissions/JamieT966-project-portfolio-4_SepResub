from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm

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
        # return render(request, 'contact.html')
        return HttpResponse('Message sent')

    return render(request, 'contact.html')