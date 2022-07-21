from django import forms
from .models import Booking

class display_booking_form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'date_choice', 'time_choice',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            'date_choice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date format is mm/dd/yyyy'}),
            'time_choice': forms.Select(attrs={'class': 'form-control',}),
        }