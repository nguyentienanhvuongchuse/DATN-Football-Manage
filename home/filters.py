import django_filters
from django_filters import CharFilter

from yard.models import *

class YardFilter(django_filters.FilterSet):

    class Meta:
        model = Yard
        fields = ["code"]
