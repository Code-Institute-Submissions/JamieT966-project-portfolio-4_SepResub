import uuid
from django.db import models
from datetime import datetime, date, time
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, ValidationError
from django.urls import reverse

TIME_CHOICES = (
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
)

class Booking(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    phone = PhoneNumberField()
    date_choice = models.DateField("Date Choice:", auto_now_add=False, auto_now=False, blank=False, null=True)
    time_choice = models.CharField(choices=TIME_CHOICES, max_length=100)
    booking_id = models.CharField(max_length=32, null=False, editable=False)

    def save(self, *args, **kwargs):
        if not self.booking_id:
            self.booking_id = str(uuid.uuid4().hex)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name + ' , ' + str(self.date_choice) + ' , ' + str(self.time_choice) + ' , ' + self.booking_id
