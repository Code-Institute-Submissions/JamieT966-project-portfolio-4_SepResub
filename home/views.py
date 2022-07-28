from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    """
    Renders home page.
    """
    return render(request, 'index.html')