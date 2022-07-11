from django.shortcuts import render
from django.http import HttpResponse

def contact_page_view(request):
    return render(request, 'contact.html')