from rest_framework.permissions import DjangoModelPermissions, BasePermission, SAFE_METHODS

from copy import deepcopy


class CustomDjangoModelPermission(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class UnauthenticatedPost(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['POST']


class OwnUserPermission(BasePermission):
    """Object-level permission to only allow updating his own user"""
    def has_object_permission(self, request, view, obj):
        # obj here is a User instance
        return obj.id == request.user.id
