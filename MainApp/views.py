from django.shortcuts import render, get_object_or_404
import json
from pathlib import Path
from django.conf import settings
from MainApp.models import Country, Language

# Create your views here.
file_path = settings.BASE_DIR / 'country-by-languages.json'
with open(file_path, encoding='utf-8') as f:
    countries_dict = json.load(f)


def home_page(request):
    context = {
        "pagename": "Главная страница в разработке",

    }
    return render(request, 'index.html', context)


def countries_list(request):
    countries = Country.objects.all()
    context = {
        "pagename": "Список стран",
        "countries": countries
    }
    return render(request, 'country_list.html', context)


def country_page(request, name):
    country = get_object_or_404(Country, name=name)
    languages = country.lang.all()
    context = {
        "pagename": country.name,
        "languages": languages,
    }
    return render(request, "country_page.html", context)


def languages_list(request):
    lang_list = Language.objects.all()

    context = {
        "pagename": "Список языков",
        "languages": lang_list,
    }
    return render(request, 'languages_list.html', context)
