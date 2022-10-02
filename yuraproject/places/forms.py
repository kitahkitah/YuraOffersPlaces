"""Формы для приложения мест."""

from django import forms

from .models import PLACE_CATEGORY_CHOICES


class CategoryForm(forms.Form):
    """Форма для выбора категории запроса."""
    category = forms.ChoiceField(
        label='Категория',
        choices=PLACE_CATEGORY_CHOICES,
        required=True
    )
