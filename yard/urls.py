from django.urls import path
from . import views

urlpatterns = [
    path("booking", views.booking, name="manage_booking"),
    path("location", views.manage_location, name="manage_location"),
    path("yard", views.manage_yard, name="manage_yard"),
    path("newyard/", views.create_yard, name="create_yard"),
    path("detail/<pk>/", views.update_yard, name="update_yard"),
    path("delete_yard/<pk>/", views.delete_yard, name="delete_yard"),
    path("time/<pk>/", views.time_cost, name="update_time"),
    path("statistical", views.statistical, name="statistical")
]
