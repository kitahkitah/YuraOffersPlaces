"""Адреса проекта с распределением по приложениям."""

from django.contrib import admin
from django.urls import include, path

handler403 = 'core.views.csrf_failure'
handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('places.urls', namespace='places')),
]
