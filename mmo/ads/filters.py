from django_filters import FilterSet

from ads.models import Comment


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'content': ['icontains'],
        }