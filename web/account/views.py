from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from web.account.serializers import UserSerializer, UpdateUserSerializer


class UserDetailsView(APIView):
    """
    Ендпоинт для получения и обновления данных
    """
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        """
        Обработка GET-запроса для получения данных
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patсh(self, request: Request):
        """
        Обработка PATH-запроса для обновления данных пользователя имени и/или details
        """
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
