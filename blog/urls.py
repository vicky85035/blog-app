from django.urls import path
from blog.views import PostListCreate, PostListAPIView

urlpatterns = [
    path('post_list/', PostListCreate.as_view(), name='post-list-create'),
    path('<int:user_id>/post_list/',PostListAPIView.as_view(), name='post-list-api-view'),
]