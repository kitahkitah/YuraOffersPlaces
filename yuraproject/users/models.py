"""Модели для приложения пользователей."""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Переопределённая модель пользователя."""

    pass
