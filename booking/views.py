from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Booking
from .forms import DisplayBookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def BookingPageView(request):
    """
    Renders booking page.
    """
    return render(request, 'booking.html')

def BookingFormView(request):
    """
    Renders booking form.
    """
    form_info = Booking.objects.all()
    return render(request, 'booking_form.html', {'form_info': form_info})

def BookingForm(request):
    """
    Checks if form is valid then posts to back end.
    Sends email confirmation to user.
    Will display error if any field is invalid.
    """
    form = DisplayBookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date_choice = form.cleaned_data['date_choice']
            time_choice = form.cleaned_data['time_choice']  
            booking = form.save()
            booking_id = booking.booking_id
            
            send_mail(
                'Booking Confirmation',
                f'Hi {name}, you are booked in for a garden consultation on' 
                '{date_choice} at {time_choice}'
                'with the booking reference: {booking_id}.'
                'You can make changes to your booking here:'
                'https://modern-landscapes.herokuapp.com/booking/',
                'modernlandscapesgardens@gmail.com',
                [f'{email}']
            )
    return render(request, 'booking_form.html', {'form':form})


def MyBooking(request):
    """
    After receiving booking reference in email user can enter booking id on this page.
    Sends an error alert if incorrect booking reference is entered.
    """
    reference_match = None
    if 'book_ref' in request.GET:
        book_ref = request.GET['book_ref']
        reference_match = Booking.objects.filter(booking_id__icontains = book_ref)
        if not reference_match:
            messages.error(request, 'This is not a recognised booking reference, please try again.')
            return render(request, 'my_booking.html')
    return render(request, 'my_booking.html', {'reference_match':reference_match})


def EditBooking(request, item_id):
    """
    Function that allows user to edit booking after correctly entering booking reference.
    """
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
    """
    Function that allows user to delete booking after correctly entering booking reference.
    """
    item = get_object_or_404(Booking, id=item_id)
    item.delete()
    messages.success(request, 'Your booking has been deleted.')
    return render(request,'index.html')