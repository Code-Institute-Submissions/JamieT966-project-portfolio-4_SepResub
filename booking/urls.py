from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingPageView, name='booking_home'),
    path('booking_form/', views.BookingForm, name='booking'),
    path('my-booking/', views.MyBooking, name='my_booking'),
    path('edit-booking/<item_id>', views.EditBooking, name='edit_booking'),
    path('delete-booking/<item_id>', views.DeleteBooking, name='delete_booking'),
]
