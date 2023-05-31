from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role.name == 'Editor'
    
class IsBlogger(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role.name == 'Blogger'
    
    def has_object_permission(self, request, view, obj):
        if obj.created_by == request.user:
            return True
        return False
    
class IsAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin'