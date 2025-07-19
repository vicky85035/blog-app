from django.urls import path
from accounts.views import (
    UserListCreate, LoginAPIView,
    SignupAPIView, UserRetrieveUpdateDestroy,
    TestAPI, UserPostList
)

urlpatterns = [
    path('user/', UserListCreate.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy' ),
    path('login/', LoginAPIView.as_view(), name='login-api-view'),
    path('signup/', SignupAPIView.as_view(), name='signup-api-view'),
    path('testapi/<str:name>/', TestAPI.as_view(), name='test-api-view'),
    path('user/posts/', UserPostList.as_view(), name='user-post-list'),
    
]