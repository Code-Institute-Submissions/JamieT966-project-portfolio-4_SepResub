from django.db import models
from datetime import datetime, date

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    selected_date = models.DateTimeField("Selected Date: mm/dd/yyyy", auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name
