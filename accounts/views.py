from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend


from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, LoginSerializer
from .permissions import UserPermission
from .filters import UserFilter


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny ,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filter_class = UserFilter
    search_fields = ('email', 'name')

    def get_object(self):
        obj = get_object_or_404(get_user_model(), pk=self.kwargs["pk"])
        return obj

    def create(self, request, *args, **kwargs):
        if 'password' not in request.data:
            raise ValidationError(detail='password is required.')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 사용자 계정 생성
        user = get_user_model().objects.create_user(
            email=request.data['email'],
            password=request.data['password'],
            name=request.data['name'],
            nickname = request.data['nickname'],
            phone = request.data['phone'],
            gender = request.data['gender'] if 'gender' in request.data else None
        )

        # token을 생성해서 함께 리턴
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })

