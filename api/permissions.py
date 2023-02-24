from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
            # superuser can do anything
            request.user.is_authenticated and
            request.user.is_superuser or
            # author can update or delete
            obj.author == request.user
        )


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsSuperUserOrStaffReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read-only for staff
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated and request.user.is_staff:
            return True
        # full access for superuser
        return bool(
            request.user.is_authenticated and
            request.user.is_superuser
        )
