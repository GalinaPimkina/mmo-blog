from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import Profile


class Post(models.Model):
    '''модель объявлений для поиска других авантюристов'''

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = RichTextUploadingField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="post", verbose_name="Класс")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="post", verbose_name="Автор поста")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    post_slug = AutoSlugField(populate_from='title', db_index=True, unique=True, verbose_name='URL')
    closed = models.BooleanField(default=False, verbose_name="Объявление закрыто")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ads:post_detail', kwargs={'post_slug': self.post_slug})

    class Meta:
        ordering = ['-time_create']
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Category(models.Model):
    '''модель классов авантюристов'''

    name = models.CharField(max_length=50, verbose_name="Класс")
    category_slug = AutoSlugField(populate_from='name', db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Comment(models.Model):
    '''модель откликов авантюристов'''

    content = models.TextField(verbose_name='Текст')
    destination_user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="comment", verbose_name="Отклик кому")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment", verbose_name="К посту")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="author_of_comment", verbose_name="Автор отклика")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    received = models.BooleanField(default=False, verbose_name="Принят") # показывает, принят отклик или нет
    rejected = models.BooleanField(default=False, verbose_name="Отклонен")# показывает, отклонен отклик или нет
    processed = models.BooleanField(default=False, verbose_name="Обработан") # показывает, обработал ли получатель отклик

    def __str__(self):
        return f"{self.time_create} - {self.post}"

    def get_absolute_url(self):
        return reverse('ads:comment_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_create']
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"


class Subscriber(models.Model):
    '''модель подписки юзера на категории'''

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscribe", verbose_name="Юзер")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subscribe", verbose_name="Категория")


class News(models.Model):
    '''новости сервиса'''

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = RichTextUploadingField()
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    news_slug = AutoSlugField(populate_from='title', db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ads:news_detail', kwargs={'news_slug': self.news_slug})

    class Meta:
        ordering = ['-time_create']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
