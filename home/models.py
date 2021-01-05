from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
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
    reply = models.ForeignKey("Comment", null=True, related_name="replies", on_delete=models.CASCADE)

class Rating(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=  [
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.pk)

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

class ViewChart(models.Model):
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    time = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    total = models.IntegerField()

    class Meta:
        db_table = "v_chart"
        managed = False

class ViewRevenue(models.Model):
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    revenue = models.IntegerField()

    class Meta:
        db_table = "v_revenue"
        managed = False

class ViewBooking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    user_location = models.IntegerField()
    yard = models.ForeignKey(Yard, on_delete=models.DO_NOTHING)
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)
    booking =models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    phone_location = models.CharField(max_length=15)
    address_location = models.CharField(max_length=255)
    description = models.TextField()
    code =models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.DateField()
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    phone =models.CharField(max_length=255)
    address =models.CharField(max_length=255)
    class Meta:
        db_table = "v_detail"
        managed = False
