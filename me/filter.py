from cgitb import lookup
import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class orderFilter(django_filters.FilterSet):
    satart_date=DateFilter(field_name="date_created",lookup_expr='gte')
    end_date=DateFilter(field_name="date_created",lookup_expr="lte")
    #note=CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:

        model=order
        fields='__all__'
        exclude=['customer','date_created']