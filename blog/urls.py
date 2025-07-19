from django.urls import path
from blog.views import (
    # UserPostList,
    PostList,
    PostCreate,
    PostRetrieveUpdateDestroy,
    LikeList,
    LikeCreate,
    PostLikeRetrieveUpdateDestroy,
    CommentList,
    CommentCreate,
    CommentRetrieveUpdateDestroy,
    PostListApiView
)

urlpatterns = [
    # path("user_post/<int:user_id>/", UserPostList.as_view(), name='user-post-list'),
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts-test/", PostListApiView.as_view(), name="post-list"),
    path("posts/create/", PostCreate.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/",
        PostRetrieveUpdateDestroy.as_view(),
        name="post-retrieve-update-destroy",
    ),
    path('posts/like/', LikeList.as_view(), name='like-list'),
    path("posts/<int:post_id>/like/", LikeCreate.as_view(), name="like-create"),
    path(
        "posts/like/<int:pk>/",
        PostLikeRetrieveUpdateDestroy.as_view(),
        name="like-retrieve-update-destroy",
    ),
    path('posts/comments/', CommentList.as_view(), name='comment-list'),
    path("posts/<int:post_id>/comments/add/", CommentCreate.as_view(), name="comment-create"),
    path(
        "posts/comment/<int:pk>/",
        CommentRetrieveUpdateDestroy.as_view(),
        name="like-retrieve-update-destroy",
    ),
]
