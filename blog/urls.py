from django.urls import path
from blog.views import PostListCreate, PostListAPIView

urlpatterns = [
    path('post/', PostListCreate.as_view(), name='post-list-create'),
    path('<int:user_id>/post/',PostListAPIView.as_view(), name='post-list-api-view'),
]