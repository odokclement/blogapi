from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Others can only read.
    """

    def has_permission(self, request, view,):
        """
        Read permissions are allowed to any request,
        so we'll always allow GET, HEAD or OPTIONS requests.
        """
        if request.user.is_authenticated:
           return True
        return False
    def  has_object_permission(self, request, view, obj):
        """
        Write permissions are only allowed to the owner of the object.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object.
        return obj.author == request.user
       