from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

class CollegeAuthentication(BasePermission):
    def get_request_methods(request, view):
        if isinstance(view, ViewSetMixin):
            return view.action
        if isinstance(view, APIView):
            return request.method.lower()
    
    def get_required_permissions(view, request_methods):
        if hasattr(view, "request_methods"):
            return view.required_permissions.get(request_methods)
        return None
    
    def user_has_permission(user, required_permissions):
        user_permissions = set(user.get_all_permissions())
        return required_permissions in user_permissions
        
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            request_methods = self.get_request_methods(request, view)
            required_permissions = self.get_required_permissions(view, request_methods)
            return self.user_has_permission(request.user, required_permissions)
        return False
    
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request=request, view=view)
