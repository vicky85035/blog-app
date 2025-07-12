from rest_framework import serializers
from blog.models import Post, Postlike, PostComment
from accounts.models import User


class PostUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = User
        fields = ["id", "name", "email", "avatar"]

class likeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Postlike
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = PostComment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    # created_by = serializers.SerializerMethodField()
    created_by = PostUserSerializer(read_only=True)
    likes = serializers.IntegerField(source='total_likes')
    comments = serializers.IntegerField(source='total_comments')

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


