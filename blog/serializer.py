from rest_framework import serializers
from blog.models import Post
from accounts.models import User


class PostUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = User
        fields = ["id", "name", "email", "avatar"]

class PostSerializer(serializers.ModelSerializer):
    # created_by = serializers.SerializerMethodField()
    created_by = PostUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'created_by',
            'title',
            'created_at',
            'cover_image',
            'description',
        ]

    # def get_created_by(self, obj):
    #     user = User.objects.filter(id=obj.created_by.id).first()
    #     # result = {"name": user.name, "email": user.email}
    #     result = PostUserSerializer(user).data
    #     return result
