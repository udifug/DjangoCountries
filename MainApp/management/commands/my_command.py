from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from MainApp.models import Country
from DjangoCountries import settings
import json

class Command(BaseCommand):
    help = 'кастомая командa'

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / 'country-by-languages.json'
        with open(file_path, encoding='utf-8') as f:
            countries_dict = json.load(f)

            for country in countries_dict:
                Country.objects.get_or_create(name=country["country"])
                self.stdout.write(self.style.SUCCESS('success'))

