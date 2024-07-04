from django import forms

from .models import Post, News, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы """

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
            self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
            self.fields['content'].required = False


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы """

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
            self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
            self.fields['content'].required = False


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]