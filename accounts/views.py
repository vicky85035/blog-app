from django.shortcuts import render
from rest_framework import generics, status, serializers, filters, permissions
from accounts.serializers import UserSerializer, BasicUserSerializer
from accounts.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from blog.models import Post
from django.shortcuts import get_object_or_404
from blog.serializer import PostSerializer
from accounts.permissions import IsAuthorOrReadOnly
# from django.contrib.auth.models import User # Or your custom user model

class LoginAPIView(generics.GenericAPIView):
    """
    API View for user login, returning JWT access and refresh tokens.
    Uses TokenObtainPairSerializer to handle token generation.
    """
    serializer_class = TokenObtainPairSerializer # Use Simple JWT's serializer
    permission_classes = [AllowAny] # Allow unauthenticated access to this endpoint

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for user login.
        Expects 'username' and 'password' in the request data.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"detail": "Both username and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Authenticate the user using Django's built-in authenticate function
        user = authenticate(request, username=username, password=password)

        if user is not None:
            data = {}
            # If authentication is successful, generate tokens using the serializer
            serializer = self.get_serializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                # Handle validation errors from the serializer (e.g., user not found)
                return Response(
                    {"detail": "Invalid credentials.", "errors": serializer.errors},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            # Return the access and refresh tokens

            data = {
                "user": BasicUserSerializer(user).data,
                'token':serializer.validated_data
            }

            return Response(data, status=status.HTTP_200_OK)
            # return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            # If authentication fails
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED
            )


class SignupAPIView(generics.CreateAPIView):
    """
    API View for user registration (signup).
    Handles creating a new user account by explicitly calling set_password().
    """
    queryset = User.objects.all()
    # We will still use a serializer for validation, but its 'create' method
    # should be adjusted or removed if it's no longer responsible for hashing.
    # For this example, we'll assume a basic serializer or validate directly.
    # If UserRegisterSerializer's create method hashes, it will double-hash here.
    # It's better to use a simpler serializer or validate manually in this view.

    # For demonstration, let's define a minimal serializer directly within views.py
    # or assume UserRegisterSerializer has its create method adjusted not to hash.
    class MinimalUserSignupSerializer(serializers.Serializer):
        name =serializers.CharField(write_only=True, required=True)
        username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that username already exists.")]
        )
        email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")]
        )
        password = serializers.CharField(write_only=True, required=True,)

    serializer_class = MinimalUserSignupSerializer # Use this new internal serializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Handles POST requests for user registration.
        Explicitly creates the user and sets the password.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract validated data
        name = serializer.validated_data['name']
        full_name = name.split( )
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        try:
            # Create the user instance
            user = User(username=username, email=email,first_name = full_name[0], last_name = full_name[1])
            # Set the password using set_password() to ensure it's hashed correctly
            user.set_password(password)
            user.save()

            return Response(
                {"message": "User registered successfully!", "username": user.username, "email": user.email},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"detail": f"User registration failed: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['first_name','last_name', 'id']
    ordering_fields = ['first_name','no_of_posts','date_joined']

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs['pk'])
        return User.objects.filter(id=user.id)