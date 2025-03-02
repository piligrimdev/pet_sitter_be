from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор регистрации пользователя с полями
    username, email, password и status.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'status']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in User.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                "Invalid status. Must be 'client' or 'petsitter'."
            )
        return value
