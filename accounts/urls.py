from django.urls import path
from accounts.views import UserListCreate, LoginAPIView, SignupAPIView

urlpatterns = [
    path('user_list/',UserListCreate.as_view(), name='user-list-create'),
    path('login/',LoginAPIView.as_view(), name='login-api-view'),
    path('signup/',SignupAPIView.as_view(), name='signup-api-view'),
]