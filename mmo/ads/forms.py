from .models import Post, Comment, News

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class AddPostForm(forms.ModelForm):
    '''создание объявления'''
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CreateCommentForm(forms.ModelForm):
    '''создание комментария'''

    class Meta:
        model = Comment
        fields = ['content', ]


class NewsAdminForm(forms.ModelForm):
    '''создание новости(только из админ панели)'''

    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = News
        fields = '__all__'