from django.test import TestCase
from .models import Booking
from django.utils import timezone
from .forms import DisplayBookingForm
from django.urls import reverse


class BookingFormTest(TestCase):

    def dummy_test(
        self, name="John", email="john@gmail.com",
            date_choice="10-10-2022", time_choice="10:00"):
        return Booking.objects.create(name=name, email=email)

    def test_name_accuracy(self, name="John",):
        w = self.dummy_test()
        self.assertTrue(isinstance(w, Booking))

    def test_email_accuracy(self, email="john@gmail.com",):
        w = self.dummy_test()
        self.assertTrue(isinstance(w, Booking))

    def test_date_accuracy(self, date_choice="10-10-2022",):
        w = self.dummy_test()
        self.assertTrue(isinstance(w, Booking))

    def test_time_accuracy(self, time_choice="10:00",):
        w = self.dummy_test()
        self.assertTrue(isinstance(w, Booking))
