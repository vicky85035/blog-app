from django.urls import path
from accounts.views import UserListCreate, LoginAPIView, SignupAPIView, UserListAPIView

urlpatterns = [
    path('user/',UserListCreate.as_view(), name='user-list-create'),
    path('<int:user_id>/user/',UserListAPIView.as_view(), name='user-api-view' ),
    path('login/',LoginAPIView.as_view(), name='login-api-view'),
    path('signup/',SignupAPIView.as_view(), name='signup-api-view'),
]