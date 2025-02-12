from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'status', 'details']


class UpdateUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    details = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['name', 'details']
