from django.contrib import admin
from .models import Post, Category, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'time_create', 'time_update', 'closed']
    list_display_links = ['title', ]
    ordering = ['time_create', 'title']
    form = PostAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_display_links = ['name', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'destination_user', 'author', 'time_create', 'time_update', 'processed']
    ordering = ['time_create', ]