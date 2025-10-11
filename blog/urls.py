from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, TagViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
