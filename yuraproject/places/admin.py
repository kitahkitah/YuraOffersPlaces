"""Настройки админки для приложения мест."""

from django.contrib import admin

from .models import Place

admin.site.register(Place)
