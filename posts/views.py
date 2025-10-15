from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
)
from .permissions import IsAuthorOrReadOnly
from .filters import PostFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = (
        Post.objects.select_related("author", "category").prefetch_related("tags").all()
    )
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = PostFilter
    search_fields = ["title", "content", "tags__name", "author__username"]
    ordering_fields = ["published_date", "created_at", "title"]

    def get_serializer_class(self):
        if self.action in ["list"]:
            return PostListSerializer
        if self.action in ["retrieve"]:
            return PostDetailSerializer
        return PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.context["request"] = self.request
        serializer.save()

    def perform_update(self, serializer):
        serializer.context["request"] = self.request
        serializer.save()
