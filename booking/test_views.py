# from unittest
from django.test import TestCase
from django.contrib.auth.models import BookingForm


User = BookingForm()

class TestBookingForm(TestCase):

    def setUp(self):