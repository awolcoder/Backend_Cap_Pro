from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()


class UserViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    A ViewSet for managing users.
    Includes registration, user details, and authenticated user info.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Define permissions per action.
        """
        if self.action in ["register", "create"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        """
        Custom endpoint for user registration.
        Example: POST /api/users/register/
        """
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def me(self, request):
        """
        Return details of the currently authenticated user.
        Example: GET /api/users/me/
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
