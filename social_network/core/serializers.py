from django.contrib.auth import password_validation
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password')


class UserRegisterSerializer(UserSerializer):
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
