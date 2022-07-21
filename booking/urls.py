from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page_view, name='booking_home'),
    path('booking_form/', views.booking_form, name='booking'),
]
