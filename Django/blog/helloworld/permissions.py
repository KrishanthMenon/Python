from rest_framework import permissions

class IsPostPossessor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.created_by == request