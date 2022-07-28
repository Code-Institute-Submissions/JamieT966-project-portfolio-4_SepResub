from django.shortcuts import render
from django.http import HttpResponse

def our_work_page_view(request):
    """
    Renders our work/ gallery page
    """
    return render(request, 'our_work.html')