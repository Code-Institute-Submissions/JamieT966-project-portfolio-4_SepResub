from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import display_booking_form

def booking_page_view(request):
    db = Booking.objects.all()
    return render(request, 'booking.html', {'db': db})

def booking_form(request):
    form = display_booking_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form':form})#PLACEHOLDER, NEED TO REPLACE WITH THANKS PAGE

    else:
        form = display_booking_form(request.POST)
    return render(request, 'booking.html', {'form':form})