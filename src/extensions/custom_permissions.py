from rest_framework.permissions import DjangoModelPermissions, BasePermission

from copy import deepcopy


class CustomDjangoModelPermission(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class UnauthenticatedPost(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['POST']
