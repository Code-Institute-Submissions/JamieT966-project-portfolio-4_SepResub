from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page_view, name='booking'),
]
