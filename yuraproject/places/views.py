"""Представления для приложения мест."""

import os

import requests
from dadata import Dadata

from django.shortcuts import render

from .forms import CategoryForm
from .models import Place, UserRequest

DADATA_TOKEN = os.getenv('DADATA_TOKEN')
GIS_TOKEN = os.getenv('GIS_TOKEN')


def get_user_ip(request):
    """Получить IP пользователя."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def get_user_geo(ip):
    """Получить геолокацию пользователя на основе IP,
    используя сервис Dadata.
    """
    result = Dadata(DADATA_TOKEN).iplocate(ip)['data']
    return result['city'], result['geo_lon'], result['geo_lat']


def search_best_places(category, lon, lat):
    """Найти лучшие по средним оценкам 3 места в городе пользователя
    на основе выбранной категорий, используя сервис 2ГИС.
    """
    payload = {
        'key': GIS_TOKEN,
        'fields': 'items.full_address_name,items.schedule,'
                  'items.external_content,items.reviews',
        'page_size': '3',
        'rubric_id': category,
        'locale': 'ru_RU',
        'location': f'{lon},{lat}',
        'search_is_query_text_complete': 'true',
        'sort': 'rating',
    }
    best_places = requests.get('https://catalog.api.2gis.com/3.0/items',
                               params=payload).json()
    return best_places['result']['items']


def crop_data(best_places):
    """Обрезать необходимую информацию о полученных местах."""
    return [
        {
            'name': place['name'],
            'address': place['full_address_name'],
            'rating': place['reviews']['general_rating'],
            'reviews_amount': place['reviews']['general_review_count'],
        } for place in best_places
    ]


def index(request):
    """Представить форму для получения лучших мест на основе категории.
    Вернуть лучшие места.
    """
    form = CategoryForm(request.POST or None)
    user_ip = get_user_ip(request)
    city, lon, lat = get_user_geo(user_ip)
    context = {
        'form': form,
        'ip': user_ip,
        'city': city,
    }

    if form.is_valid():
        category = form.cleaned_data.pop('category')
        found_places = search_best_places(category, lon, lat)
        best_places = crop_data(found_places)
        context.update({'best_places': best_places})

        if request.user.is_authenticated:
            user_request = UserRequest.objects.create(category=category, city=city,
                                                      user=request.user)
            list_of_places = [Place(**place) for place in best_places]
            user_request.place_set.set(list_of_places, bulk=False)
    return render(request, 'places/index.html', context)
