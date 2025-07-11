from django.urls import path
from blog.views import PostListCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('post/', PostListCreate.as_view(), name='post-list-create'),
    path('<int:pk>/post/',PostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
]