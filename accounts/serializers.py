from rest_framework import serializers
from accounts.models import User
from blog.models import Post
from blog.serializer import PostSerializer, LikeSerializer, CommentSerializer

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','cover_image','description']

class UserSerializer(serializers.ModelSerializer):
    # post_list = serializers.SerializerMethodField()
    post_list = UserPostSerializer(source='post_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'date_joined',
            'email',
            'post_list',
        ]

    # def get_post_list(self, obj):
    #     result = Post.objects.filter(created_by__id=obj.id).all()
    #     data = []
    #     for post in result:

    #         data.append({
    #             "id": post.id,
    #             'title': post.title,
    #             'images':post.cover_image,
    #             "created_at": post.created_at,
    #         })
    #     # data = PostSerializer(result, many=True).data
    #     return data

class PostUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = User
        fields = ["id", "name", "email", "avatar"]
        
class UserPostListSerializer(serializers.ModelSerializer):
    created_by = PostUserSerializer(read_only=True)
    likes = LikeSerializer(source='post_likes', many=True, read_only=True)
    comments = CommentSerializer(source='post_comments', many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'created_by',
            'title',
            'created_at',
            'cover_image',
            'description',
            'likes',
            'comments'
        ]
        
class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'avatar', 'username']