from django import forms
from .models import Booking
from django.forms import ModelForm

class DateInput(forms.DateInput):
    """
    Method for displaying date picker found on Stack Overflow by user: "avi"
    """
    input_type = 'date'

class DisplayBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'date_choice', 'time_choice',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            'date_choice': DateInput(attrs={'class': 'form-control'}),
            'time_choice': forms.Select(attrs={'class': 'form-control',}),
        }