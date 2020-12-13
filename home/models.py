from django.db import models
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
    note = models.TextField(null=True, blank=True)
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)

    def price(self):
        return self.time.cost
