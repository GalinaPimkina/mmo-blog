from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name="Никнейм")
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Аватар")
    token = models.CharField(max_length=6, null=True, blank=True, verbose_name='Токен')

    class Meta:
        verbose_name = "Авантюрист"
        verbose_name_plural = "Авантюристы"

    def __str__(self):
        return self.nickname

