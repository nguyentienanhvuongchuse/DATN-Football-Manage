from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("location/<obj>/", views.follow_location, name="fl"),
    path("contact/", views.contact, name = "contact"),
    path("cart/", views.cart, name = "cart"),
    path("history/", views.cart_history, name = "history"),
    path("detail/<str:pk>/", views.detail, name = "detail"),
    path("time/<str:pk>/",views.time_booking, name = "time_booking"),
    path("booking/<str:pk>/", views.booking_yard, name="booking_yard"),
    path('email_send',views.sendEmai,name="send_mail"),
    path("information/", views.information, name = "user"),
    path("changepw/", views.change_pw, name = "change_pw"),
    path("login/", views.signin, name = "login"),
    path("signup/", views.signup, name = "signup"),
    path("logout/", views.logout_user, name = "logout"),

    path("tk/", views.thanhkhe, name = "tk"),
    path("st/", views.sontra, name = "st"),
    path("nhs/", views.nhs, name = "nhs"),
    path("lc/", views.lienchieu, name = "lc"),
    path("hc/", views.haichau, name = "hc"),
    path("cl/", views.camle, name = "cl"),
    path("hv/", views.hoavang, name = "hv"),

    path("rate/", views.rate, name="rate")
]
