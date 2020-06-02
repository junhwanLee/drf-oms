from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import *
from .permissions import OrderPermission


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (OrderPermission, )
    serializer_class = OrderSerializer

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs["pk"])
        return obj

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

