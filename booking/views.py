from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import DisplayBookingForm

def BookingPageView(request):
    return render(request, 'booking.html')

def BookingFormView(request):
    form_info = Booking.objects.all()
    form_class = DisplayBookingForm()
    return render(request, 'booking_form.html', {'form_info': form_info})

def BookingForm(request):
    form = DisplayBookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'booking.html', {'form':form})#PLACEHOLDER, NEED TO REPLACE WITH THANKS PAGE

    else:
        form = DisplayBookingForm(request.POST or None)
    return render(request, 'booking_form.html', {'form':form})