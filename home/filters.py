import django_filters
from django_filters import CharFilter

from yard.models import *

class LocationFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr="icontains",label="Tên sân")
    class Meta:
        model = Location
        fields = ["name"]
