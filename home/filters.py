import django_filters
from django_filters import CharFilter, DateFilter
from django import forms
from yard.models import *
from .models import *

class LocationFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr="icontains",label="Tên sân")
    class Meta:
        model = Location
        fields = ["name"]

class BookingFilter(django_filters.FilterSet):
    date = DateFilter(field_name="date",lookup_expr="icontains",label="Ngay")
    class Meta:
        model = BookingView
        fields = ["date","type","time"]
