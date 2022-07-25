from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingPageView, name='booking_home'),
    path('booking_form/', views.BookingForm, name='booking'),
    path('my-booking/', views.MyBooking, name='my_booking'),
]
