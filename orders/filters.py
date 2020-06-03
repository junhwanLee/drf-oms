# from django_filter
from django_filters import rest_framework as d_filters
from .models import *


class OrderFilter(d_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['customer', 'product_name']