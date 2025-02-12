from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from web.account.serializers import UserSerializer, UpdateUserSerializer


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):

        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request: Request):
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(update_fields=['name', 'details'])
            return Response(serializer.data)

        return Response(serializer.error_messages)
