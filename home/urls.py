from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name = "contact"),
    path("cart/", views.cart, name = "cart"),
    path("detail/<str:pk>/", views.detail, name = "detail"),
    path("time/<str:pk>/",views.time_booking, name = "time_booking"),
    path("booking/<str:pk>/", views.booking_yard, name="booking_yard"),

    path("login/", views.signin, name = "login"),
    path("signup/", views.signup, name = "signup"),
    path("logout/", views.logout_user, name = "logout")
]
