import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
published_date = django_filters.DateFromToRangeFilter()
category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
author = django_filters.CharFilter(field_name='author__username', lookup_expr='iexact')
tags = django_filters.CharFilter(method='filter_tags')


class Meta:
model = Post
fields = ['category', 'author', 'tags']


def filter_tags(self, queryset, name, value):
# allow comma separated tags
tag_names = [t.strip() for t in value.split(',')]
return queryset.filter(tags__name__in=tag_names).distinct()