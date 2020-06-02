from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    allowed_actions = ['login', 'create']

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            # only allowed in allowed actions
            if view.action in UserPermission.allowed_actions:
                return True
            else:
                return False
        else:
            return True

    # def has_object_permission(self, request, view, obj):
    #     # admin 이면 True
    #     if request.user.is_admin:
    #         return True
    #
    #     # 일반 유저인 경우
    #     if request.user != obj:
    #         return False
