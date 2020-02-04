from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'created', 'likes')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self):
        user = User(email=self.validated_data['email'],
                    username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords mush match'})
        user.set_password(password)
        user.save()
        return user


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True)

    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
