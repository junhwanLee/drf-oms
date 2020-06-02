# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    name = serializers.RegexField(regex=r'^[a-zA-Z가-힣]+$', min_length=2, max_length=20)
    nickname = serializers.RegexField(regex=r'^[a-z]+$', min_length=2, max_length=30)
    password = serializers.RegexField(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)',
        min_length=10
    )

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name', 'nickname', 'phone', 'gender', 'password')
        write_only_fields = ('password',)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        # user = authenticate(**data)
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")