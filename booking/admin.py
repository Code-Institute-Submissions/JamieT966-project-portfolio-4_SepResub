from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    """
    creates a read only field for booking id in admin panel.
    """
    readonly_fields = (['booking_id'])


admin.site.register(Booking, BookingAdmin)