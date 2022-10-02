"""Представления для приложения пользователей."""

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from places.models import UserRequest
from .forms import EditForm


@login_required
def my_profile(request):
    """Представить профиль текущего пользователя."""
    page_number = request.GET.get('page')
    user_requests = (UserRequest.objects.prefetch_related('place_set')
                     .filter(user=request.user))
    requests_page_obj = Paginator(user_requests, 1).get_page(page_number)

    context = {
        'user': request.user,
        'requests_page_obj': requests_page_obj,
    }
    return render(request, 'users/my_profile.html', context)


@login_required
def edit_my_profile(request):
    """Изменить профиль текущего пользователя."""
    form = EditForm(request.POST or None, instance=request.user)

    if form.is_valid():
        if form.cleaned_data.pop('is_clearing_history'):
            request.user.previous_requests.all().delete()
        request.user.save()
        return redirect('users:my_profile')
    return render(request, 'users/edit_my_profile.html', {'form': form})
