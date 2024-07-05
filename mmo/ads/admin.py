from django.contrib import admin

from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'time_create', 'time_update', 'closed']
    list_display_links = ['title', ]
    ordering = ['time_create', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_display_links = ['name', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'destination_user', 'author', 'time_create', 'time_update', 'processed']
    ordering = ['time_create', ]

