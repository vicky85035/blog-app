from rest_framework import serializers
from blog.models import Post
from accounts.models import UserProfile

class PostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source= 'user.name')
    category = serializers.CharField(source= 'story_by')
    
    class Meta:
        model = Post
        fields = [
            'name',
            'category',
            'title',
            'created_at',
        ]