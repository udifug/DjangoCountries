from django.shortcuts import render
import json
from pathlib import Path
from django.conf import settings

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
    # with open(file_path, encoding='utf-8') as f:
    #     countries_dict = json.load(f)
    # for countries in countries_dict['country']:
    #     country = countries['country']

    context = {
        "pagename": "Список стран",
        "countries": countries_dict
    }
    return render(request, 'country_list.html', context)


def country_page(request, name):
    for country in countries_dict:
        if country["country"] == name:
            context = {
                "pagename": country["country"],
                "languages": country["languages"]
            }
            return render(request,"country_page.html", context)




def languages_list(request):
    lang_list = set()
    for countries in countries_dict:
        for lang in countries.get("languages"):
            lang_list.add(lang)

    context = {
        "pagename": "Список языков",
        "languages": lang_list,
    }
    return render(request, 'languages_list.html', context)
