from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Booking
from .forms import DisplayBookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings


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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date_choice = form.cleaned_data['date_choice']
            time_choice = form.cleaned_data['time_choice']
            form.save()
            if 'book_ref' in request.GET:
                book_ref = request.GET['book_ref']
                booking_id = Booking.objects.filter(booking_id__icontains = book_ref)
                send_mail(
                    'Booking Confirmation',
                    f'Hi {name}, you are booked in for a garden consultation on {date_choice} at {time_choice} with the booking reference: {booking_id}',
                    'modernlandscapesgardens@gmail.com',
                    [f'{email}']
                )
                return render(request, 'booking.html', {'form':form})

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


def EditBooking(request, item_id):
    item = get_object_or_404(Booking, id=item_id)
    if request.method == 'POST':
        form = DisplayBookingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been changed successfully.')
            return render(request,'index.html')
    form = DisplayBookingForm(instance = item)
    context = {'form': form}
    return render(request,'edit_booking.html', context)


def DeleteBooking(request, item_id):
    item = get_object_or_404(Booking, id=item_id)
    item.delete()
    messages.success(request, 'Your booking has been deleted.')
    return render(request,'index.html')