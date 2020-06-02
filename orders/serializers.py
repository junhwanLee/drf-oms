from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    order_number = serializers.RegexField(
        regex=r'^[0-9A-Z]+$', min_length=12, max_length=12
    )
    product_name = serializers.CharField(max_length=100)

    class Meta:
        model = Order
        fields = ('customer', 'order_number', 'product_name', 'paymented_at')
