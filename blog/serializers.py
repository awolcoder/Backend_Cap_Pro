from rest_framework import serializers
from .models import Post, Category, Tag, User


# ---- USER SERIALIZER ----
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# ---- CATEGORY SERIALIZER ----
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ---- TAG SERIALIZER ----
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# ---- POST SERIALIZER ----
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), source='tags', write_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'body', 'author',
            'category', 'category_id', 'tags', 'tag_ids',
            'created_at', 'updated_at'
        ]
