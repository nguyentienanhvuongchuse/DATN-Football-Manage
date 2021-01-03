from django.urls import path
from . import views

urlpatterns = [
    path("booking", views.booking, name="manage_booking"),
    path("location", views.manage_location, name="manage_location"),
    path("open", views.booking_open, name="location_open"),
    path("close", views.booking_close, name="location_close"),
    path("accept", views.booking_accept, name="location_accept"),
    path("yard", views.manage_yard, name="manage_yard"),
    path("newyard/", views.create_yard, name="create_yard"),
    path("detail/<pk>/", views.update_yard, name="update_yard"),
    path("delete_yard/<pk>/", views.delete_yard, name="delete_yard"),
    path("time/<pk>/", views.time_cost, name="create_time"),
    path("updatetime/<pk>/", views.update_timecost, name="update_time"),
    path("deletetime/<pk>/", views.delete_timecost, name="delete_time"),
    path("statistical", views.statistical, name="statistical"),
    path("total", views.resultData, name="total"),
    path("timedata/<str:pk>/", views.timeAjax, name="timeajax"),
]
