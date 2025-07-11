from django.urls import path
from blog.views import PostListCreate, PostRetrieveUpdateDestroy, PostViewSet

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('<slug:tag_slug>/post/',PostViewSet.as_view({'get': 'list'}), name='post-view-set'),
    path('<int:pk>/post/',PostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
]