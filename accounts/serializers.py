# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from orders.serializers import OrderSerializer
from orders.models import Order


class UserSerializer(serializers.ModelSerializer):
    name = serializers.RegexField(regex=r'^[a-zA-Z가-힣]+$', min_length=2, max_length=20)
    nickname = serializers.RegexField(regex=r'^[a-z]+$', min_length=2, max_length=30)
    password = serializers.RegexField(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)',
        min_length=10,
        write_only=True
    )
    phone = serializers.RegexField(regex=r'^[0-9]+$', min_length=7, max_length=20)
    email = serializers.EmailField(max_length=100)
    last_order = serializers.SerializerMethodField()

    def get_last_order(self, user):
        order = Order.objects.filter(customer=user).last()
        return None if order is None else OrderSerializer(instance=order).data

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name', 'nickname', 'phone', 'gender', 'password', 'last_order')
        # write_only_fields = ('password',)
        # extra_kwargs = {'password': {'write_only': True}}
        # read_only_fields = ('id', 'email', 'name', 'nickname', 'phone', 'gender', 'last_order')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.RegexField(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)',
        min_length=10,
    )

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")