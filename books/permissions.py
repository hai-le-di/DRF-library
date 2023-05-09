from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminWriteOnly(BasePermission):
    """
    Permission class that only allows admin users to create, update,
    partially update, or delete objects, while authenticated users can
    view objects and unauthenticated users can only list objects.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            # allow read-only access for all authenticated and
            # unauthenticated users
            return True
        else:
            # only allow write access for admin users
            return request.user and request.user.is_staff
