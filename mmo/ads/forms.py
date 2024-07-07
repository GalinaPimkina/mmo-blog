from .models import Post, Comment

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class AddPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]