from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
        )

class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj:User):
        if obj.username == request.user.username or request.user.is_superuser == True:
            return True
        
        return False
    
