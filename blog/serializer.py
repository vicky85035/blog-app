from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source= 'user.name')
    category = serializers.CharField(source= 'story_by')

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'category',
            'title',
            'created_at',
            'cover_image',
            'description',
        ]