from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        allowed_actions = ['login', 'create']
        if not request.user.is_authenticated:
            # only allowed in allowed actions
            if view.action in allowed_actions:
                return True
            else:
                return False
        else:
            return True
