from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers.registration_serializers import (
    UserRegistrationSerializer
)


class UserRegistrationView(APIView):
    """
    Вью для регистрации пользователя с полями
    username, email, password, status.
    """

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "Результат": "Регистрация успешно завершена",
                "username": serializer.validated_data.get('username'),
                "email": serializer.validated_data.get('email'),
                "status": serializer.validated_data.get('status')
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
