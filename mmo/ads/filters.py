from django_filters import FilterSet

from ads.models import Post, Comment


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'content': ['icontains'],
        }


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'content': ['icontains'],
        }