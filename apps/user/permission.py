from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role.name == 'Editor'
    
class IsBlogger(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role.name == 'Blogger'
    
class IsAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin'