from django_filters import FilterSet

from ads.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }