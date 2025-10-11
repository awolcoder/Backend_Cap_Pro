from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Category, Tag, User
from .serializers import PostSerializer, CategorySerializer, TagSerializer, UserSerializer


# ---- USER VIEWSET ----
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---- CATEGORY VIEWSET ----
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ---- TAG VIEWSET ----
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ---- POST VIEWSET ----
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author', 'category').prefetch_related('tags')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
