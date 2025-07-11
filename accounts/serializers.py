from rest_framework import serializers
from accounts.models import User
from blog.models import Post

class UserSerializer(serializers.ModelSerializer):
    no_of_posts = serializers.SerializerMethodField()
    list_of_posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'date_joined',
            'email',
            'no_of_posts',
            'list_of_posts',
        ]

    def get_no_of_posts(self, obj):
        return Post.objects.filter(created_by__id=obj.id).count()

    def get_list_of_posts(self, obj):
        result = Post.objects.filter(created_by__id=obj.id).all()
        data = []
        for post in result:

            data.append({
                "id": post.id,
                'title': post.title,
                'images':post.cover_image,
                "created_at": post.created_at,
            })
        # data = PostSerializer(result, many=True).data
        return data