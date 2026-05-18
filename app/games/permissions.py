from rest_framework.permissions import BasePermission


class IsCreatorOrAdmin(BasePermission):
    """
    Разрешение только для создателя игры или администратора
    """

    def has_object_permission(self, request, view, obj):
        # Проверяем является ли пользователь создателем или админом
        return obj.creator == request.user or request.user.is_staff
