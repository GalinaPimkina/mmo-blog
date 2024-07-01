from django_filters import FilterSet

from ads.models import Post, Comment


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'content': ['icontains'],
        }


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'content': ['icontains'],
        }