from django.urls import path
from accounts.views import UserListCreate, LoginAPIView, SignupAPIView, UserRetrieveUpdateDestroy

urlpatterns = [
    path('user/',UserListCreate.as_view(), name='user-list-create'),
    path('user/<int:pk>/',UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy' ),
    path('login/',LoginAPIView.as_view(), name='login-api-view'),
    path('signup/',SignupAPIView.as_view(), name='signup-api-view'),
]