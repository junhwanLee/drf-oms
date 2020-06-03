from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .permissions import OrderPermission
from .filters import OrderFilter


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (OrderPermission, )
    serializer_class = OrderSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filter_class = OrderFilter
    search_fields = (
        'customer__name', 'customer__email',
        'order_number', 'product_name',
    )

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs["pk"])
        return obj

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

