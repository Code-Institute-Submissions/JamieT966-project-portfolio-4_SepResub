from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    readonly_fields = (['booking_id'])


admin.site.register(Booking, BookingAdmin)