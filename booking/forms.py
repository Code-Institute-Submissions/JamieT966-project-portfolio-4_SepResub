from django import forms
from .models import Booking

class display_booking_form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'selected_date',)