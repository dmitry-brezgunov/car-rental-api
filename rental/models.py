from django.contrib.auth.models import AbstractUser
from django.db import models


class Language(models.TextChoices):
    RU = ('RU', 'Русский')
    EN = ('EN', 'English')


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    lang = models.CharField(max_length=50, choices=Language.choices)
    REQUIRED_FIELDS = []


class Car(models.Model):
    name_en = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    creation_year = models.PositiveSmallIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_ru


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car, related_name='rentals')
