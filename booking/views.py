from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import DisplayBookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError

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


def MyBooking(request):
    if 'book_ref' in request.GET:
        book_ref = request.GET['book_ref']
        reference_match = Booking.objects.filter(booking_id__icontains = book_ref)
        return render(request, 'my_booking.html', {'reference_match':reference_match})
    else:
        # CURRENTLY BOOK_REF LINKED TO INPUT NOT BUTTON, HAVE TO FIND WAY TO GET THIS TO WORK BELOW
        # messages.error(request, 'This is not a recognised booking reference, please try again.')
        return render(request, 'my_booking.html')
