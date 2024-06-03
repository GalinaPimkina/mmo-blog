from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Avatar")

