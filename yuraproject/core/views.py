"""Представления для ошибок HTTP."""

from django.shortcuts import render


def csrf_failure(request, reason=''):
    """Представить ошибку 403/CSRF."""
    return render(request, 'core/403.html', status=403)


def page_not_found(request, exception):
    """Представить ошибку 404."""
    return render(request, 'core/404.html', status=404)
