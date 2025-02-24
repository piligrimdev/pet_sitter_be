from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from users.serializers.users_serializers import (
    UsersListSerializer, UserAllFieldSerializer, UpdateUserSerializer
)

User = get_user_model()


class UsersListView(APIView):
    """Вью для получения списка пользователей."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UsersListSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailsView(APIView):
    """Вью для получения и редактирования раздела details пользователя."""

    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        serializer = UserAllFieldSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request: Request):
        serializer = UpdateUserSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save(update_fields=['name', 'details'])
            return Response(serializer.data)

        return Response(serializer.error_messages)
