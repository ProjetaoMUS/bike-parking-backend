from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """Permission class that allows the user to see any user, but only edit their own."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
