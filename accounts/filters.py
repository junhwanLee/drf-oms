# from django_filter
from django_filters import rest_framework as d_filters
from .models import *


class UserFilter(d_filters.FilterSet):
    class Meta:
        model = User
        fields = ['email', 'gender']