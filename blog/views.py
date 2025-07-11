from django.shortcuts import render
from rest_framework import generics, filters, viewsets
from blog.models import Post
from accounts.models import User
from blog.serializer import PostSerializer
from blog.pagination import SetPagination
from django.shortcuts import get_object_or_404
# from taggit.models import Tag

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__first_name', 'user__last_name']
    ordering_fields = ['user__first_name', 'created_at']
    pagination_class = SetPagination

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs['pk'])
        return Post.objects.filter(user__id=user.id)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     breakpoint()
    #     tag = get_object_or_404(Tag, slug='tag_slug')
    #     return Post.objects.filter(tags__name=tag.name)

    def get_queryset(self):
        queryset = self.queryset
        tag_names = self.request.query_params.get('tags')
        if tag_names:
            tags = [tag.strip() for tag in tag_names.split(',')]
            # Filter posts that have ALL specified tags
            # For "OR" logic (any of the tags): posts = queryset.filter(tags__name__in=tags).distinct()
            for tag in tags:
                queryset = queryset.filter(tags__name=tag)
        return queryset.distinct()



