from django.shortcuts import render
from django.http import HttpResponse

def our_work_page_view(request):
    return render(request, 'our_work.html')