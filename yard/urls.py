from django.urls import path
from . import views

urlpatterns = [
    path("booking", views.booking, name="Booking"),
    path("location", views.manage_location, name="manage_location"),
    path("yard", views.manage_yard, name="manage_yard"),
    path("statistical", views.statistical, name="statistical")
]
