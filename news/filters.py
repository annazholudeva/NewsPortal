from django.forms import DateInput
from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'type': ['icontains'],
            'category': ['icontains'],
            'date': ['gt'],
        }