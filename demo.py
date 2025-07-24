import json


with open("country-by-languages.json", encoding='utf-8') as f:
    countries_dict = json.load(f)
    # lang_list = []
    # for countries in countries_dict:
    #     for lang in countries.get("languages"):
    #         print(lang)
    for countries in countries_dict:

        print(countries)