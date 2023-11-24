from rest_framework.permissions import BasePermission,  SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.status == "B":
            return True
        return False
    

class IsRedactor(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.status == "A":
            return True
        return False


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.authors == request.user


