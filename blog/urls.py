from django.urls import path
from blog.views import PostListCreate

urlpatterns = [
    path('post_list/', PostListCreate.as_view(), name='post-list-create'),
]