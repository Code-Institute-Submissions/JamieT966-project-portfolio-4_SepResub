from django.test import TestCase
from .models import Booking
from django.utils import timezone
from .forms import DisplayBookingForm
from django.urls import reverse


class FormsTest(TestCase):

    def test_valid_form(self):
        dummy_content = Booking.objects.create(
            name="John",
            email="john@gmail.com",
            phone="+353861204773",
            date_choice="2022-10-10",
            time_choice="10:00")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_form_name_empty(self):
        dummy_content = Booking.objects.create(
            name="",
            email="john@gmail.com",
            phone="+353861204773",
            date_choice="2022-10-10",
            time_choice="10:00")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_form_email_invaild(self):
        dummy_content = Booking.objects.create(
            name="John",
            email="john.com",
            phone="+353861204773",
            date_choice="2022-10-10",
            time_choice="10:00")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_form_phone_wrong(self):
        dummy_content = Booking.objects.create(
            name="John",
            email="john@gmail.com",
            phone="apple",
            date_choice="2022-10-10",
            time_choice="10:00")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_form_date_past(self):
        dummy_content = Booking.objects.create(
            name="John", email="john@gmail.com",
            phone="+353861204773",
            date_choice="2020-10-10",
            time_choice="10:00")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_form_time_not_in_select(self):
        dummy_content = Booking.objects.create(
            name="John",
            email="john@gmail.com",
            phone="+353861204773",
            date_choice="2022-10-10",
            time_choice="10:15")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_form_date_error(self):
        dummy_content = Booking.objects.create(
            name="John",
            email="john@gmail.com",
            phone="+353861204773",
            date_choice="2020-10-10",
            time_choice="10:00")
        data = {
            'name': dummy_content.name,
            'email': dummy_content.email,
            'phone': dummy_content.phone,
            'date_choice': dummy_content.date_choice,
            'time_choice': dummy_content.time_choice}
        form = DisplayBookingForm(data=data)
        self.assertRaisesMessage(
            Exception, "You have selected either today's date or a past date.")
