from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_work_page_view, name='work'),
]
