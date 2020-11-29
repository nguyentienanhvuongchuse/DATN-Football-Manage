from django.db import models
from yard.models import *
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    STATUS = (
        ("XL", "Xử lý"),
        ("XN", "Xác nhận"),
        ("TC", "Từ chối")
    )
    time_id = models.ForeignKey(Time, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length = 255, choices=STATUS)
    note = models.TextField()
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)
