from django.db import models
from django.utils import timezone
from yard.models import *
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    STATUS = (
        ("M", "Mở"),
        ("XL", "Xử lý"),
        ("XN", "Xác nhận"),
        ("TC", "Từ chối")
    )
    time = models.ForeignKey(Time, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length = 255, choices=STATUS, default="M")
    date = models.DateField(default=timezone.now, blank=True)
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)

    def price(self):
        return self.time.cost

class DetailUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class BookingView(models.Model):
    id = models.BigIntegerField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    yard = models.ForeignKey(Yard, on_delete=models.DO_NOTHING)
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)
    booking =models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    user_booking = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    description = models.TextField()
    code =models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()
    class Meta:
        db_table = "v_booking"
        managed = False

class LocationView(models.Model):
    id = models.BigIntegerField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    yard = models.ForeignKey(Yard, on_delete=models.DO_NOTHING)
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    description = models.TextField()
    code =models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    class Meta:
        db_table = "v_location"
        managed = False

class CartView(models.Model):
    id = models.BigIntegerField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    yard = models.ForeignKey(Yard, on_delete=models.DO_NOTHING)
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)
    booking =models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    user_booking = models.IntegerField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    description = models.TextField()
    code =models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()
    class Meta:
        db_table = "booking_view"
        managed = False
