from django.contrib import admin
from .models import *
from yard.models import *
# Register your models here.


class DisplayBooking(admin.ModelAdmin):
    list_display = ["user", "time","status", "price"]

admin.site.register(Booking,DisplayBooking)
