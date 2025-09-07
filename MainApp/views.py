from django.contrib.admin.templatetags.admin_list import pagination
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
import json
from pathlib import Path
from django.conf import settings
from MainApp.models import Country, Language


def home_page(request):
    context = {
        "pagename": "Главная страница в разработке",

    }
    return render(request, 'index.html', context)


def countries_list(request):
    countries = Country.objects.all()
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "pagename": "Список стран",
        "countries": countries,
        'page_obj': page_obj
    }
    return render(request, 'country_list.html', context)


def country_page(request, name):
    country = get_object_or_404(Country, name=name)
    languages = country.lang.all()
    context = {
        "pagename": f"Страна: {country.name}",
        "languages": languages,
    }
    return render(request, "country_page.html", context)


def languages_list(request):
    lang_list = Language.objects.all()
    paginator = Paginator(lang_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "pagename": "Список языков",
        "languages": lang_list,
        'page_obj': page_obj
    }
    return render(request, 'languages_list.html', context)


def language_page(request, name):
    language = get_object_or_404(Language, name=name)
    countries = language.countries.all()
    context = {
        "pagename": f"Язык: {language.name}",
        "language": language,
        'countries': countries
    }
    return render(request, 'language_page.html', context)
