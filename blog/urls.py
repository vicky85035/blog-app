from django.urls import path
from blog.views import (
    PostList,
    PostCreate,
    PostRetrieveUpdateDestroy,
    LikeList,
    LikeCreate,
    LikeRetrieveUpdateDestroy,
    CommentCreate,
    CommentRetrieveUpdateDestroy,
)

urlpatterns = [
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/create/", PostCreate.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/",
        PostRetrieveUpdateDestroy.as_view(),
        name="post-retrieve-update-destroy",
    ),
    path("posts/<int:post_id>/like/", LikeCreate.as_view(), name="like-create"),
    path(
        "posts/like/<int:pk>/",
        LikeRetrieveUpdateDestroy.as_view(),
        name="like-retrieve-update-destroy",
    ),
    path("posts/comment/", CommentCreate.as_view(), name="like-create"),
    path(
        "posts/comment/<int:pk>/",
        CommentRetrieveUpdateDestroy.as_view(),
        name="like-retrieve-update-destroy",
    ),
]
