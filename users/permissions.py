from django.views import View
from rest_framework import permissions
from users.models import User


class EmployeePermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return request.user.is_authenticated and (
            request.user.is_employee or obj == request.user
        )
