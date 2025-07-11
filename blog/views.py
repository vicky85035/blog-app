from django.shortcuts import render
from rest_framework import generics, filters
from blog.models import Post
from accounts.models import UserProfile
from blog.serializer import PostSerializer
from blog.pagination import SetPagination
from django.shortcuts import get_object_or_404

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__first_name', 'user__last_name']
    ordering_fields = ['user__first_name', 'created_at']
    pagination_class = SetPagination
    
class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = get_object_or_404(UserProfile, id=self.kwargs['user_id'])
        return Post.objects.filter(user__id=user.id).order_by('-created_at')
    