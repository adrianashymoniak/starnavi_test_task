from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
