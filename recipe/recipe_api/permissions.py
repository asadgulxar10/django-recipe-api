from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnRecipe(permissions.BasePermission):
    """Allows users to update their recipies"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to edit their own recipies"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user