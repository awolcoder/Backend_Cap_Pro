from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
from categories.serializers import CategorySerializer
from tags.serializers import TagSerializer
from tags.models import Tag
from categories.models import Category

User = get_user_model()


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "category",
            "tags",
            "published_date",
            "created_at",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("author", "created_at", "updated_at")


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, required=False
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Post
        fields = ("id", "title", "content", "category_id", "tag_ids", "published_date")

    def create(self, validated_data):
        tag_ids = validated_data.pop("tag_ids", [])
        category = validated_data.pop("category_id", None)
        post = Post.objects.create(
            author=self.context["request"].user, category=category, **validated_data
        )
        if tag_ids:
            post.tags.set(tag_ids)
        return post

    def update(self, instance, validated_data):
        tag_ids = validated_data.pop("tag_ids", None)
        category = validated_data.pop("category_id", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if category is not None:
            instance.category = category
        instance.save()
        if tag_ids is not None:
            instance.tags.set(tag_ids)
        return instance

