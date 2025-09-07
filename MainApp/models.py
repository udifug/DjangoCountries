from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lang = models.ManyToManyField(Language, related_name='countries')
