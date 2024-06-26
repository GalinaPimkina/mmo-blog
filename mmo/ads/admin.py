from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Category, Comment, News

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(News)


