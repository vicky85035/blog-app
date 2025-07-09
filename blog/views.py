from django.shortcuts import render
from rest_framework import generics, filters
from blog.models import Post
from blog.serializer import PostSerializer
from blog.pagination import SetPagination

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__first_name', 'user__last_name']
    ordering_fields = ['user__first_name', 'created_at']
    pagination_class = SetPagination
