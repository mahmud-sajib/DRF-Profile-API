from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    
    """Allow users to update their own profile"""
    def has_object_permission(self, request, view, obj):

        """Allow user to view any profile if it's a GET method(SAFE_METHODS)"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        """Check if the user has the permission to edit their profile in case of PUT, PATCH & DELETE method"""
        return obj.id == request.user.id # returns True or False