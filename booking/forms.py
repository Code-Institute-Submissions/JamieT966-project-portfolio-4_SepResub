from django import forms
from .models import Booking
from django.forms import ModelForm
from datetime import date
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    """
    Method for displaying date picker found on Stack Overflow by user: "avi".
    """
    input_type = 'date'


class DisplayBookingForm(forms.ModelForm):
    """
    Main booking form.
    """
    class Meta:
        """
        Class to define booking form fields and widgets.
        """
        model = Booking
        fields = ('name', 'email', 'phone', 'date_choice', 'time_choice',)

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                                'placeholder': 'Please enter your name',
                                'name': 'name'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control',
                                'placeholder':
                                    'Please enter your email address'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control',
                                'placeholder':
                                    'Please enter your phone number'}),
            'date_choice': DateInput(attrs={'class': 'form-control'}),
            'time_choice': forms.Select(attrs={'class': 'form-control '}),
        }

    def clean_date_choice(self, *args, **kwargs):
        """
        Validates that selected date is not today or a past date.
        """
        date_choice = self.cleaned_data.get('date_choice')
        if date_choice <= date.today():
            self.add_error(
                "date_choice",
                "You have selected either today's date or a past date.")
        return date_choice
