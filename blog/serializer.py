from rest_framework import serializers
from blog.models import Post, Postlike, PostComment
from accounts.models import User


class PostUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = User
        fields = ["id", "name", "email", "avatar"]

class LikeSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Postlike
        fields = ['id', 'user_id', 'name','created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = PostUserSerializer(source="user", read_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'author', 'created_at', 'text']


class PostSerializer(serializers.ModelSerializer):
    # created_by = serializers.SerializerMethodField()
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
            'comments',
        ]

    # def get_created_by(self, obj):
    #     user = User.objects.filter(id=obj.created_by.id).first()
    #     # result = {"name": user.name, "email": user.email}
    #     result = PostUserSerializer(user).data
    #     return result

class PostLikeSerializer(serializers.ModelSerializer):
    user = PostUserSerializer(read_only=True)
    class Meta:
        model = Postlike
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"
