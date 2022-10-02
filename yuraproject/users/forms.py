"""Формы для приложения пользователей."""

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreationForm(UserCreationForm):
    """Форма для создания пользователя."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class EditForm(forms.ModelForm):
    """Форма для изменения пользователя."""

    is_clearing_history = forms.BooleanField(label='Очистить историю мест?',
                                             initial=False, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
