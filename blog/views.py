from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.permissions import IsAuthenticated
from blog.models import Post, Postlike, PostComment
from accounts.models import User
from blog.serializer import PostSerializer, LikeSerializer, CommentSerializer,PostLikeSerializer, PostCommentSerializer
from blog.pagination import SetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# from taggit.models import Tag

# class UserPostList(generics.ListAPIView):
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         user = get_object_or_404(User, id=self.kwargs["user_id"])
#         return Post.objects.filter(created_by__id=user.id)

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_by__first_name", "created_at"]
    pagination_class = SetPagination

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        queryset = Post.objects.all()
        if user_id:
            queryset = queryset.filter(created_by_id=user_id)
        return queryset

from rest_framework.views import APIView
class PostListApiView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id")
        posts = Post.objects.all()

        if user_id:
            result = posts.filter(created_by_id = user_id)
            serializer_obj = PostSerializer(result, many=True)
            post_data = serializer_obj.data
        else:
            post_data = PostSerializer(posts, many=True).data
        return Response(post_data)


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs["pk"])


class LikeList(generics.ListAPIView):
    queryset = Postlike.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class LikeCreate(generics.CreateAPIView):
    queryset = Postlike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get("post_id")

        if Postlike.objects.filter(user=request.user, post_id=post_id).exists():
            return Response(
                {"detail": "You have already liked this post."},
                status=400
            )

        serializer = self.get_serializer(data={"post": post_id})
        serializer.is_valid(raise_exception=True)

        try:
            like_instance = serializer.save(user=request.user)
        except Exception as e:
            return Response(
                {"detail": f"An error occurred while saving the like: {e}"},
                status=500
            )

        return Response(
            {"message": "Post liked successfully!", "id": like_instance.id},
            status=201
        )

class PostLikeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Postlike.objects.filter(id=self.kwargs["pk"])


class CommentList(generics.ListAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentCreate(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get("post_id")
        serializer = self.get_serializer(
            data={
                "post": post_id,
                "user": request.user.id,
                "text": request.data.get("text")
            }
        )
        serializer.is_valid(raise_exception=True)

        try:
            comment_instance = serializer.save(
                # user=request.user,
                # text=request.data["text"]
            )

        except Exception as e:
            return Response(
                {"detail": f"An error occurred while saving the like: {e}"},
                status=500
            )

        return Response(
            {"message": "Post comment is  successfully done!", "id": comment_instance.id},
            status=201
        )

class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PostComment.objects.filter(id=self.kwargs["pk"])
