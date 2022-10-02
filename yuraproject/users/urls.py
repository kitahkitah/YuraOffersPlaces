"""Адреса для приложения пользователей."""

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CreationForm
from .views import edit_my_profile, my_profile

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        CreateView.as_view(
            template_name='users/signup.html',
            form_class=CreationForm,
            success_url=reverse_lazy('places:index'),
        ),
        name='signup',
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout',
    ),
    path(
        'my_profile/edit/password/',
        PasswordChangeView.as_view(
            template_name='users/change_password.html',
            success_url=reverse_lazy('users:my_profile'),
        ),
        name='change_password',
    ),
    path('my_profile/edit/', edit_my_profile, name='edit_my_profile'),
    path('my_profile/', my_profile, name='my_profile'),
]
