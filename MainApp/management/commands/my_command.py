from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from MainApp.models import Country, Language
from DjangoCountries import settings
import json

class Command(BaseCommand):
    help = 'кастомая командa'

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / 'country-by-languages.json'
        with open(file_path, encoding='utf-8') as f:
            countries_dict = json.load(f)

            for country in countries_dict:
                country_obj, create_country = Country.objects.get_or_create(name=country["country"])


                for lang in country.get('languages',[]):
                    lang_obj, create_lang = Language.objects.get_or_create(name=lang)
                    country_obj.lang.add(lang_obj)

                self.stdout.write(self.style.SUCCESS(f'success add {country_obj.name} and {lang_obj.name}'))


