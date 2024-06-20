from django import forms

from .models import Post, News, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]