from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from blog.models import Post, Postlike, PostComment
from accounts.models import User
from blog.serializer import PostSerializer, LikeSerializer, PostLikeSerializer, PostCommentSerializer
from blog.pagination import SetPagination
from django.shortcuts import get_object_or_404

# from taggit.models import Tag


# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user__first_name", "user__last_name"]
    ordering_fields = ["user__first_name", "created_at"]
    pagination_class = SetPagination


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Postlike.objects.filter(id=self.kwargs["pk"])


class CommentList(generics.ListAPIView):
    queryset = Postlike.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class CommentCreate(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCommentSerializer

    def get_queryset(self):
        return PostComment.objects.filter(id=self.kwargs["pk"])
