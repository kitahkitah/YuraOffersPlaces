"""Настройки админки для приложения пользователей."""

from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
