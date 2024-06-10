from django.contrib.auth.models import AbstractUser
from django.db import models
from autoslug import AutoSlugField


class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name="Nickname")
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Avatar")

    def __str__(self):
        return self.nickname


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField() # д/б текст, картинки, видео и тд
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="post", verbose_name="Category")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="post", verbose_name="Author")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    post_slug = AutoSlugField(populate_from='title', db_index=True, unique=True, verbose_name='Slug')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category")
    icon = models.ImageField(upload_to="icons/", verbose_name="Icon")
    category_slug = AutoSlugField(populate_from='name', db_index=True, unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment", verbose_name="Comment")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment", verbose_name="Author")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"{self.time_create} - {self.post}"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name="Content") # д.б текст картинки видео и тд
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="news", verbose_name="Author")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    news_slug = AutoSlugField(populate_from='title', db_index=True, unique=True, verbose_name='Slug')

    def __str__(self):
        return f"{self.time_create} - {self.title}"
