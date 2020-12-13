from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Location(models.Model):
    DISTRIC = (
        ("TK","Quận Thanh Khê"),
        ("ST","Quận Sơn Trà"),
        ("NHS","Quận Ngũ Hành Sơn"),
        ("LC","Quận Liên Chiểu"),
        ("HC","Quận Hải Châu"),
        ("CL","Quận Cẩm Lệ"),
        ("HV","Huyện Hoà Vang"),
        ("HS","Huyện Hoàng Sa")
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255, choices=DISTRIC)
    description = RichTextUploadingField()
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Yard(models.Model):
    TYPE = (
        ("5", "5 người"),
        ("7", "7 người"),
        ("11", "11 người")
    )
    location = models.ForeignKey(Location, null=True, on_delete = models.CASCADE)
    code = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPE)
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.code

class Time(models.Model):
    TIME = (
        ("5:00","5:00"),
        ("6:00","6:00"),
        ("7:00","7:00"),
        ("8:00","8:00"),
        ("9:00","9:00"),
        ("10:00","10:00"),
        ("11:00","11:00"),
        ("12:00","12:00"),
        ("13:00","13:00"),
        ("14:00","14:00"),
        ("15:00","15:00"),
        ("16:00","16:00"),
        ("17:00","17:00"),
        ("18:00","18:00"),
        ("19:00","19:00"),
        ("20:00","20:00"),
        ("21:00","21:00"),
        ("22:00","22:00")
    )
    yard = models.ForeignKey(Yard, null=True, on_delete=models.CASCADE)
    time = models.CharField(max_length=255, choices=TIME)
    cost = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True,blank=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.time
