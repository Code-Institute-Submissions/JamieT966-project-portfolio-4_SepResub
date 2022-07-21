from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import display_booking_form

def booking_page_view(request):
    return render(request, 'booking.html')

def booking_form_view(request):
    form_info = Booking.objects.all()
    form_class = display_booking_form()
    return render(request, 'booking_form.html', {'form_info': form_info})

def booking_form(request):
    form = display_booking_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form':form})#PLACEHOLDER, NEED TO REPLACE WITH THANKS PAGE

    else:
        form = display_booking_form(request.POST or None)
    return render(request, 'booking_form.html', {'form':form})