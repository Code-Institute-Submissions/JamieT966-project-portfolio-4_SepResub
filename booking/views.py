from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import DisplayBookingForm
from django.contrib import messages

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
            # messages.success(request, 'Thanks for getting in touch. A member of the Modern Landscapes team will get back to you shortly.')
            return render(request, 'booking.html', {'form':form})#PLACEHOLDER, NEED TO REPLACE WITH THANKS PAGE

    else:
        form = DisplayBookingForm(request.POST or None)
    return render(request, 'booking_form.html', {'form':form})