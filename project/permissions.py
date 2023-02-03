from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserEditDeletePermission(BasePermission):
    message = 'Editing nominations is just for the user who created it'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.createdBy == request.user