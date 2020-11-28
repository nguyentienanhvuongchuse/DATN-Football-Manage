from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name = "contact"),
    path("order/", views.order, name = "order"),
    path("detail/", views.detail, name = "detail"),
    path("login/", views.login, name = "login"),
    path("signup/", views.signup, name = "signup")
]
