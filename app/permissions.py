from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    
    """Allow users to update their own profile"""
    def has_object_permission(self, request, view, obj):

        """Allow user to view any profile if it's a GET request(SAFE_METHODS)"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        """Check if the user has the permission to edit their profile. If True it will allow PUT, PATCH & DELETE operations"""
        return obj.id == request.user.id # returns True or False


class UpdateOwnStatus(permissions.BasePermission):
    
    """Allow users to update their own status"""
    def has_object_permission(self, request, view, obj):

        """Allow user to view their profile if it's a GET request(SAFE_METHODS)"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        """Check if the user has the permission to edit their profile. If True it will allow PUT, PATCH & DELETE operations"""
        return obj.user_profile.id == request.user.id # returns True or False