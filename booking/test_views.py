from django.test import TestCase
from .models import Booking
from django.utils import timezone
from .forms import DisplayBookingForm
from django.urls import reverse
from django.core import mail


class ViewsTest(TestCase):

    def test_view_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    def test_view_booking_home_page(self):
        response = self.client.get(reverse('booking_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'booking.html')

    def test_view_booking_page(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'booking_form.html')

    def test_view_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'contact.html')

    def test_view_work_page(self):
        response = self.client.get(reverse('work'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'our_work.html')

    def test_view_my_booking_page(self):
        response = self.client.get(reverse('my_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'my_booking.html')

    def test_valid_form_phone_error(self):
        dummy_content = Booking.objects.create(
            name="",
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
        self.assertRaisesMessage(
            Exception, "Enter a valid phone number (e.g. +12125552368).")

    def test_valid_form_name_error(self):
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
        self.assertRaisesMessage(Exception, "Please fill out this field.")

    def test_valid_form_email_error(self):
        dummy_content = Booking.objects.create(
            name="",
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
        self.assertRaisesMessage(Exception, "Enter a valid email address.")


class EmailTest(TestCase):

    def test_send_email(self):
        """
        Taken from Stack Overflow, user: Davor Lucic
        """
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
