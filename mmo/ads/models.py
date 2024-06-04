from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name="Nickname")
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Avatar")


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField() # д/б текст, картинки, видео и тд
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="post", verbose_name="Category")


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category")


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment", verbose_name="Comment")