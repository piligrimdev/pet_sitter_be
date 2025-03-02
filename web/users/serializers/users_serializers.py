from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAllFieldSerializer(serializers.ModelSerializer):
    """Сериализатор с полным набором полей пользователя."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'status', 'details']


class UpdateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования данных пользователя."""

    name = serializers.CharField(max_length=100)
    details = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'details']


class UsersListSerializer(serializers.ModelSerializer):
    """Сериализатор выводы списка пользователей."""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'status']
