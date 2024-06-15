from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name="Nickname")
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Avatar")

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name='Текст') # д/б текст, картинки, видео и тд
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="post", verbose_name="Класс")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="post", verbose_name="Автор поста")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    post_slug = AutoSlugField(populate_from='title', db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ads:post_detail', kwargs={'post_slug': self.post_slug})


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Класс")
    icon = models.ImageField(upload_to="icons/", verbose_name="Иконка")
    category_slug = AutoSlugField(populate_from='name', db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(verbose_name='Текст')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment", verbose_name="К посту")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment", verbose_name="Автор комментария")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def __str__(self):
        return f"{self.time_create} - {self.post}"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name="Текст") # д.б текст картинки видео и тд
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="news", verbose_name="Автор новости")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    news_slug = AutoSlugField(populate_from='title', db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return f"{self.time_create} - {self.title}"
