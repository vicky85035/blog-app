from rest_framework import serializers
from blog.models import Post
from accounts.models import UserProfile

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source= 'user.name')
    category = serializers.CharField(source= 'story_by')
    post_images = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'category',
            'title',
            'created_at',
            'post_images',
            'description',
        ]

    def get_post_images(self,obj):
        if not obj.post_img:
            return "No Images"